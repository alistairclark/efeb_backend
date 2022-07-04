from django.contrib import admin

from efeb_backend.stock_items.models import Category, Manufacturer, StockItem


class StockItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(StockItem, StockItemAdmin)
