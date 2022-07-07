import django_filters

from efeb_backend.products.models import Product


class ProductFilter(django_filters.FilterSet):
    manufacturer = django_filters.CharFilter(
        field_name="manufacturer", method="filter_manufacturer"
    )
    categories = django_filters.CharFilter(
        field_name="categories", method="filter_categories"
    )

    def filter_manufacturer(self, queryset, name, value):
        manufacturer_slugs = value.split(",")
        return queryset.filter(manufacturer__slug__in=manufacturer_slugs).distinct()

    def filter_categories(self, queryset, name, value):
        category_slugs = value.split(",")
        return queryset.filter(categories__slug__in=category_slugs).distinct()

    class Meta:
        model = Product
        fields = ["manufacturer", "categories"]
