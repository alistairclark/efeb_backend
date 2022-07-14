from django.urls import path

from efeb_backend.orders.views import checkout, stripe_webhook

app_name = "orders"
urlpatterns = [
    path("", checkout, name="checkout"),
    path("stripe-webhook/", stripe_webhook, name="stripe-webhook"),
]
