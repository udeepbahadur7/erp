from rest_framework import routers

from supply.api.items.views import StockGroupModelViewSet, ItemLineUpdateDeleteModelViewSet, \
    ItemLineCreateModelViewSet

router = routers.DefaultRouter()
router.register("items/", StockGroupModelViewSet, base_name="stock-group")
router.register("itemline/", ItemLineUpdateDeleteModelViewSet, base_name="itemline")
router.register("(?P<group>[\d]+)/itemline/", ItemLineCreateModelViewSet, base_name="itemline")

urlpatterns = [] + router.urls
