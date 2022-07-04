from django.contrib import admin
from django.urls import include, path

from efeb_backend.api import urls as api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls, namespace="api")),
]
