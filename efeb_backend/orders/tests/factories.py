import factory

from efeb_backend.orders.models import Order, OrderItem


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem
