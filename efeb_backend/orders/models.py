import uuid

from django.db import models
from django.db.models import F

from efeb_backend.products.models import Product
from efeb_backend.orders.choices import ORDER_STATUSES


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=ORDER_STATUSES, max_length=7)

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
