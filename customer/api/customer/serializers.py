from rest_framework import serializers


from customer.models import Customer
from customer.api.agent.serializers import AgentSerializer
from customer.api.billing_address.serializers import BillingAddressSerializer
from customer.api.contact_person.serializers import ContactPersonSerializer
from customer.api.shipping_address.serializers import ShippingAddressSerializer


class CustomerSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    billing_addresses = BillingAddressSerializer(source='billingaddress_set',many=True)
    contact_persons = ContactPersonSerializer(source='contactperson_set',many=True)
    shippingaddresses = ShippingAddressSerializer(source='shippingaddress_set',many=True)
    class Meta:
        model = Customer
        fields = '__all__'