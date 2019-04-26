from rest_framework import viewsets


from customer.models import ShippingAddress
from .serializers import ShippingAddressSerializer


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
