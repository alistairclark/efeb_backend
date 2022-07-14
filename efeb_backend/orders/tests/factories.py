import factory

from efeb_backend.orders.models import Order


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
