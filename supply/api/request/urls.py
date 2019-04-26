from rest_framework import routers

from supply.api.request.views import PurchaseRequestModelViewSet

router = routers.DefaultRouter()
router.register("", PurchaseRequestModelViewSet, base_name="purchase-request")

urlpatterns = [] + router.urls
