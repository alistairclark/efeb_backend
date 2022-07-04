from django.contrib import admin

from efeb_backend.products.models import Category, Manufacturer, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}


class ManufcaturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufcaturerAdmin)
admin.site.register(Product, ProductAdmin)
