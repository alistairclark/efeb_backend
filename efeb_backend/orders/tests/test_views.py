from unittest.mock import MagicMock, patch

from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from efeb_backend.orders.choices import SUCCESS

from efeb_backend.orders.models import OrderItem
from efeb_backend.products.tests.factories import ProductFactory
from efeb_backend.orders.tests.data import (
    multiple_items_json,
    multiples_of_one_item_json,
    stripe_webhook_data,
    insufficient_stock_data,
)
from efeb_backend.orders.tests.factories import OrderFactory, OrderItemFactory


class TestCheckout(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("orders:checkout")
        self.product_1 = ProductFactory(slug="canyon", stock_count=10)
        self.product_2 = ProductFactory(slug="metal-zone-mt-2", stock_count=5)

        self.mocked_session = MagicMock()
        self.mocked_session.url = "http://example.com"

    @patch("efeb_backend.orders.views.stripe")
    def test_checkout_multiple_items(self, mocked_stripe):
        mocked_stripe.checkout.Session.create.return_value = self.mocked_session

        response = self.client.post(
            self.url,
            data=multiple_items_json,
        )
        mocked_stripe.checkout.Session.create.assert_called()
        assert (response.status_code, 302)

        _, kwargs = mocked_stripe.checkout.Session.create.call_args

        assert len(kwargs.get("line_items")) == 2
        assert OrderItem.objects.count() == 2
        assert len(mail.outbox) > 0

    @patch("efeb_backend.orders.views.stripe")
    def test_checkout_single_item(self, mocked_stripe):
        mocked_stripe.checkout.Session.create.return_value = self.mocked_session

        self.client.post(
            self.url,
            data=multiples_of_one_item_json,
        )

        _, kwargs = mocked_stripe.checkout.Session.create.call_args
        assert kwargs.get("line_items")[0].get("quantity") == 4
        assert OrderItem.objects.count() == 1

    @patch("efeb_backend.orders.views.stripe")
    def test_checkout_not_enough_stock(self, mocked_stripe):
        mocked_stripe.checkout.Session.create.return_value = self.mocked_session

        response = self.client.post(
            self.url,
            data=insufficient_stock_data,
        )

        assert response.status_code == 400


class TestWebhook(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("orders:stripe-webhook")
        self.product = ProductFactory(stock_count=5)
        self.order = OrderFactory(
            uuid=stripe_webhook_data.get("data")
            .get("object")
            .get("client_reference_id")
        )
        self.order_item = OrderItemFactory(
            product=self.product, order=self.order, quantity=3
        )

    @patch("efeb_backend.orders.views.stripe")
    def test_webhook(self, mocked_stripe):
        mocked_stripe.Webhook.construct_event.return_value = stripe_webhook_data
        self.client.post(self.url, data={}, **{"Stripe-Signature": "test"})
        mocked_stripe.Webhook.construct_event.assert_called()
        self.order.refresh_from_db()

        assert self.order.status == SUCCESS
        assert self.order.email == "test@example.com"
        assert self.order.total_amount_pence == 4500

        self.product.refresh_from_db()

        assert self.product.stock_count == 2
