from rest_framework import viewsets


from customer.models import Agent
from .serializers import AgentSerializer


class  AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
