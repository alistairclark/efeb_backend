from rest_framework import viewsets
from efeb_backend.api.filters import ProductFilter

from efeb_backend.api.serializers import (
    CategorySerializer,
    ManufacturerSerializer,
    ProductSerializer,
)
from efeb_backend.products.models import Category, Manufacturer, Product


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = [
        "display_name",
        "manufacturer__display_name",
        "categories__display_name",
    ]
    filterset_class = ProductFilter
