from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from supply.api.vendors.serializers import VendorModelSerializer, ReminderModelSerializer
from supply.models.vendors import Vendor


class VendorModelViewSet(viewsets.ModelViewSet):
    serializer_class = VendorModelSerializer
    queryset = Vendor.objects.all()
    search_fields = ["name", "address_street", "address_city", "address_state"]
    ordering_fields = ["name", "mobile", "address_street", "balance"]

    def get_serializer_class(self):
        if self.action == "create_reminder":
            return ReminderModelSerializer
        return super(VendorModelViewSet, self).get_serializer_class()

    @action(methods=["POST"], detail=True)
    def create_reminder(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, vendor=instance)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=400)
        return Response(data=dict(), status=201)
