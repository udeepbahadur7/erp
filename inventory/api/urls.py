from django.urls import path
from rest_framework import routers

from inventory.api.views import StockViewSet


router = routers.DefaultRouter()
router.register("stocks", StockViewSet, base_name="stock")

urlpatterns = [
] + router.urls
