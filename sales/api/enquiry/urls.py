from rest_framework import routers


from sales.api.enquiry.viewsets import EnquiryViewSet

router = routers.DefaultRouter()
router.register('', EnquiryViewSet, base_name='enquiry')

urlpatterns = router.urls
