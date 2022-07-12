from django.contrib import admin
from django.urls import include, path

from efeb_backend.api import urls as api_urls
from efeb_backend.orders import urls as orders_urls

urlpatterns = [
    path("checkout/", include(orders_urls, namespace="orders")),
    path("admin/", admin.site.urls),
    path("api/", include(api_urls, namespace="api")),
]
