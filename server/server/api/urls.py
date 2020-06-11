from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    ShopViewSet,
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'shops', ShopViewSet)

urlpatterns = router.urls
