from rest_framework import viewsets


from customer.models import ContactPerson
from .serializers import ContactPersonSerializer


class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
