import factory

from efeb_backend.products.models import Category, Manufacturer, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    slug = factory.Sequence(lambda n: "category%s" % n)
    display_name = factory.Sequence(lambda n: "Category %s" % n)

    class Meta:
        model = Category


class ManufacturerFactory(factory.django.DjangoModelFactory):
    slug = factory.Sequence(lambda n: "manufacturer%s" % n)
    display_name = factory.Sequence(lambda n: "Manufacturer %s" % n)

    class Meta:
        model = Manufacturer


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    price = 60
    stock_count = 10
    slug = factory.Sequence(lambda n: "Product%s" % n)
    display_name = factory.Sequence(lambda n: "Stock Item %s" % n)
