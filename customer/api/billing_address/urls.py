from rest_framework import routers


from customer.api.billing_address.viewsets import BillingAddressViewSet

router = routers.DefaultRouter()
router.register('', BillingAddressViewSet, base_name='billing_address')

urlpatterns = router.urls
