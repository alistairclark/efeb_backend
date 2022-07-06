from rest_framework import serializers

from efeb_backend.products.models import Category, Manufacturer, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["id"]


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        exclude = ["id"]
