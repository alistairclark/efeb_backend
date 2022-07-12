import json
from unittest.mock import MagicMock, patch

from django.test import Client, TestCase
from django.urls import reverse


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
            data={
                "cart": json.dumps(
                    [{"price": "10", "display_name": "test", "quantity": 1}]
                )
            },
        )
        mocked_stripe.checkout.Session.create.assert_called()
        assert (response.status_code, 302)

        _, kwargs = mocked_stripe.checkout.Session.create.call_args

        assert len(kwargs.get("line_items")) == 1

        response = self.client.post(
            self.url,
            data={
                "cart": json.dumps(
                    [{"price": "10", "display_name": "test", "quantity": 3}]
                )
            },
        )

        _, kwargs = mocked_stripe.checkout.Session.create.call_args
        assert len(kwargs.get("line_items")) == 3
