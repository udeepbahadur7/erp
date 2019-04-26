from rest_framework import viewsets
from rest_framework.decorators import action

from supply.api.request.serializers import PurchaseRequestModelSerializer
from supply.models.request import PurchaseRequest


class PurchaseRequestModelViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseRequestModelSerializer
    queryset = PurchaseRequest.objects.all()

    @action(methods=["POST"], detail=True)
    def create_purchase_order(self, request, *args, **kwargs):
        raise NotImplementedError

    @action(methods=["POST"], detail=True)
    def email(self, request, *args, **kwargs):
        raise NotImplementedError

    @action(methods=["POST"], detail=True)
    def download(self, request, *args, **kwargs):
        raise NotImplementedError
