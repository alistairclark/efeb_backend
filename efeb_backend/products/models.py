from django.db import models
from ckeditor.fields import RichTextField


class Manufacturer(models.Model):
    display_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.display_name


class Category(models.Model):
    display_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.display_name


class Product(models.Model):
    display_name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    picture = models.ImageField()
    stock_count = models.IntegerField()
    description = RichTextField()
    categories = models.ManyToManyField(Category)
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    links = RichTextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.display_name
