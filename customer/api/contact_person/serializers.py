from rest_framework import serializers


from customer.models import ContactPerson


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'