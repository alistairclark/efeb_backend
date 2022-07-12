import uuid

from django.db import models

from efeb_backend.orders.choices import ORDER_STATUSES


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=ORDER_STATUSES, max_length=7)
