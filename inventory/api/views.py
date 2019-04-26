from rest_framework import viewsets

from inventory.api.serializers import StockSerializer
from inventory.models import Stock


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    permission_classes = []  # todo
    serializer_class = StockSerializer
