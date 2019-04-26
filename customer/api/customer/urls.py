from rest_framework import routers


from customer.api.customer.viewsets import CustomerViewSet

router = routers.DefaultRouter()
router.register('', CustomerViewSet, base_name='customer')

urlpatterns = router.urls
