import django_filters

from efeb_backend.products.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ["manufacturer__slug", "categories__slug"]
