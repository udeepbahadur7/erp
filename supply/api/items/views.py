from rest_framework import viewsets, mixins

from supply.api.items.serializers import StockGroupModelSerializer, ItemLineModelSerializer
from supply.models.items import StockGroup, ItemLine


class StockGroupModelViewSet(mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    """This view-set will simply create itemlines and associate it to the
    appropriate request/order."""
    serializer_class = StockGroupModelSerializer
    permission_classes = []
    queryset = StockGroup.objects.none()


class ItemLineUpdateDeleteModelViewSet(mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       viewsets.GenericViewSet):
    """This view-set will simply update/destroy itemline."""
    serializer_class = ItemLineModelSerializer
    permission_classes = []
    queryset = ItemLine.objects.all()


class ItemLineCreateModelViewSet(mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    """This view-set will simply update/destroy itemline."""
    serializer_class = ItemLineModelSerializer
    permission_classes = []
    queryset = ItemLine.objects.all()

    def get_serializer_context(self):
        context = super(ItemLineCreateModelViewSet, self).get_serializer_context()
        context["group"] = self.request.parser_context["kwargs"]["group"]
        return context
