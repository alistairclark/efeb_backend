import uuid

from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

from efeb_backend.products.models import Product
from efeb_backend.orders.choices import ORDER_STATUSES, PENDING


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=ORDER_STATUSES, max_length=7, default=PENDING)
    customer_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    total_amount_pence = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.uuid} ({self.status})"

    def decrement_stock(self):
        for item in self.items.all():
            item.product.stock_count = item.product.stock_count - item.quantity
            item.product.save()

    def notify_admin(self):
        send_mail(
            "New order received",
            "A new order has been received.",
            "efeb@efeb.store",
            ["alistairclark89@gmail.com"],
            fail_silently=False,
        )

    def notify_customer(self):
        send_mail(
            "Your order has been placed",
            render_to_string("emails/checkout_confirmed.html", {"order": self}),
            "efeb@efeb.store",
            [self.email],
            fail_silently=False,
        )

    def get_display_total_amount_pence(self):
        if self.total_amount_pence is not None:
            return f"£{self.total_amount_pence/100}"
        return "£0"

    def get_display_address(self):
        if self.address_line_2 != "":
            return (
                "{name}, {address_line_1}, {address_line_2}, {city}, {postcode}".format(
                    self.customer_name,
                    self.address_line_1,
                    self.address_line_2,
                    self.city,
                    self.postcode,
                )
            )

        return (
            f"{self.customer_name}, {self.address_line_1}, {self.city}, {self.postcode}"
        )

    def get_display_details(self):
        items = ""
        for item in self.items.all():
            items += f"<p>{item.product.display_name} x{item.quantity}</p>"

        return items


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="order_items"
    )
    quantity = models.IntegerField()
