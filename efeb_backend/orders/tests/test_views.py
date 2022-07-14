import json
from unittest.mock import MagicMock, patch

from django.test import Client, TestCase
from django.urls import reverse
from efeb_backend.orders.choices import SUCCESS

from efeb_backend.orders.tests.data import (
    multiple_items_json,
    multiples_of_one_item_json,
    stripe_webhook_data,
)
from efeb_backend.orders.tests.factories import OrderFactory


class TestCheckout(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("orders:checkout")

    @patch("efeb_backend.orders.views.stripe")
    def test_checkout(self, mocked_stripe):
        mocked_session = MagicMock()
        mocked_session.url = "http://example.com"
        mocked_stripe.checkout.Session.create.return_value = mocked_session

        response = self.client.post(
            self.url,
            data=multiple_items_json,
        )
        mocked_stripe.checkout.Session.create.assert_called()
        assert (response.status_code, 302)

        _, kwargs = mocked_stripe.checkout.Session.create.call_args

        assert len(kwargs.get("line_items")) == 2

        response = self.client.post(
            self.url,
            data=multiples_of_one_item_json,
        )

        _, kwargs = mocked_stripe.checkout.Session.create.call_args
        assert kwargs.get("line_items")[0].get("quantity") == 4


class TestWebhook(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("orders:stripe-webhook")
        self.order = OrderFactory(
            uuid=stripe_webhook_data.get("data")
            .get("object")
            .get("client_reference_id")
        )

    @patch("efeb_backend.orders.views.stripe")
    def test_webhook(self, mocked_stripe):
        mocked_stripe.Webhook.construct_event.return_value = stripe_webhook_data
        self.client.post(self.url, data={}, STRIPE_SIGNATURE="test")
        mocked_stripe.Webhook.construct_event.assert_called()
        self.order.refresh_from_db()

        assert self.order.status == SUCCESS
