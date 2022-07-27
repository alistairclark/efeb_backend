import uuid

from django.db import models

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

    def __str__(self):
        return f"{self.uuid} ({self.status})"

    def decrement_stock(self):
        for item in self.items.all():
            item.product.stock_count = item.product.stock_count - item.quantity
            item.product.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="order_items"
    )
    quantity = models.IntegerField()
