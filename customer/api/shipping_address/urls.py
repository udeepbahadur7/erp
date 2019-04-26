from rest_framework import routers


from customer.api.contact_person.viewsets import ShippingAddressViewSet

router = routers.DefaultRouter()
router.register('', ShippingAddressViewSet, base_name='shipping_address')

urlpatterns = router.urls
