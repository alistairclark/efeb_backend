from django.contrib import admin

from efeb_backend.orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]

    list_display = ["uuid", "created_at"]


admin.site.register(Order, OrderAdmin)
