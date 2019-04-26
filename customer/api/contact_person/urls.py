from rest_framework import routers


from customer.api.contact_person.viewsets import ContactPersonViewSet

router = routers.DefaultRouter()
router.register('', ContactPersonViewSet, base_name='contact_person')

urlpatterns = router.urls
