from django.urls import path

from efeb_backend.orders.views import checkout, order_success, order_cancelled

app_name = "orders"
urlpatterns = [
    path("", checkout, name="checkout"),
    path("success", order_success, name="order-success"),
    path("cancelled", order_cancelled, name="order-cancelled"),
]
