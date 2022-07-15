from django.test import Client, TestCase
from django.urls import reverse

from efeb_backend.products.tests.factories import (
    CategoryFactory,
    ManufacturerFactory,
    ProductFactory,
)


class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list(self):
        list_url = reverse("api:category-list")
        response = self.client.get(list_url)

        assert response.status_code == 200


class ManufacturerTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list(self):
        list_url = reverse("api:manufacturer-list")
        response = self.client.get(list_url)

        assert response.status_code == 200


class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = ProductFactory()
        self.list_url = reverse("api:product-list")

    def test_detail(self):
        response = self.client.get(
            reverse("api:product-detail", kwargs={"slug": self.product.slug})
        )

        assert response.status_code == 200
        assert response.json().get("slug") == self.product.slug

    def test_list(self):
        response = self.client.get(self.list_url)

        assert response.status_code == 200
        assert response.json()[0].get("slug") == self.product.slug

    def test_filter_by_manufacturer(self):
        manufacturer = ManufacturerFactory()
        product_by_manufacturer = ProductFactory(manufacturer=manufacturer)

        response = self.client.get(f"{self.list_url}?manufacturer={manufacturer.slug}")

        assert response.json()[0].get("slug") != self.product.slug
        assert response.json()[0].get("slug") == product_by_manufacturer.slug

        other_manufacturer = ManufacturerFactory()
        self.product.manufacturer = other_manufacturer
        self.product.save()

        response = self.client.get(
            f"{self.list_url}?manufacturer={manufacturer.slug},{other_manufacturer.slug}"
        )

        assert response.json()[0].get("slug") == self.product.slug
        assert response.json()[1].get("slug") == product_by_manufacturer.slug

    def test_filter_by_categories(self):
        category_1 = CategoryFactory()
        category_2 = CategoryFactory()

        product_category_1 = ProductFactory()
        product_category_1.categories.add(category_1)

        product_category_2 = ProductFactory()
        product_category_2.categories.add(category_2)

        response = self.client.get(f"{self.list_url}?categories={category_1.slug}")

        assert len(response.json()) == 1
        assert response.json()[0].get("slug") == product_category_1.slug

        response = self.client.get(
            f"{self.list_url}?categories={category_1.slug},{category_2.slug}"
        )

        assert len(response.json()) == 2

    def test_search(self):
        manufacturer = ManufacturerFactory()
        category = CategoryFactory()

        # We never expect this product to show up
        ProductFactory()

        self.product.manufacturer = manufacturer
        self.product.save()
        self.product.categories.add(category)

        response = self.client.get(f"{self.list_url}?search={category.display_name}")

        assert len(response.json()) == 1
        assert response.json()[0].get("slug") == self.product.slug

        response = self.client.get(
            f"{self.list_url}?search={manufacturer.display_name}"
        )

        assert len(response.json()) == 1
        assert response.json()[0].get("slug") == self.product.slug

        response = self.client.get(
            f"{self.list_url}?search={self.product.display_name}"
        )

        assert len(response.json()) == 1
        assert response.json()[0].get("slug") == self.product.slug
