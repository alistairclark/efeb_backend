from rest_framework import routers

from efeb_backend.api.views import CategoryViewSet, ManufacturerViewSet, ProductViewSet


router = routers.SimpleRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("manufacturers", ManufacturerViewSet, basename="manufacturer")
router.register("products", ProductViewSet, basename="product")

app_name = "api"
urlpatterns = router.urls
