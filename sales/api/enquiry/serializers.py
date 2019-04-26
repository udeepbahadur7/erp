from rest_framework import serializers

from sales.models import Enquiry


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
        # depth = 2

    # itemline = serializers.IntegerField(source='itemline')