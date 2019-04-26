from rest_framework import routers

from supply.api.vendors.views import VendorModelViewSet

router = routers.DefaultRouter()
router.register("", VendorModelViewSet, base_name="vendor")
# reminders urls

urlpatterns = router.urls
