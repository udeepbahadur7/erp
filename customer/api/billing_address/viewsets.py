from rest_framework import viewsets


from customer.models import BillingAddress
from .serializers import BillingAddressSerializer


class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
