from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    ShopViewSet,
)
from django.conf.urls import include, url
from server.api.views import user_info

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'shops', ShopViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^current_user_info/', user_info)]
