from rest_framework import routers


from customer.api.agent.viewsets import AgentViewSet

router = routers.DefaultRouter()
router.register('', AgentViewSet, base_name='agent')

urlpatterns = router.urls
