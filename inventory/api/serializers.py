from rest_framework import serializers

from inventory.models import Stock
from libs.constants import RENTAL_CHOICES


class StockSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField("inventory:stock-detail")
    rental = serializers.MultipleChoiceField(choices=RENTAL_CHOICES)

    class Meta:
        model = Stock
        exclude = []
        extra_kwargs = dict(
            last_purchase_amount=dict(read_only=True),
            average_amount=dict(read_only=True),
            image=dict(required=True),
        )

    def get_field_names(self, declared_fields, info):
        if self.context["view"].action == "list":
            return ['name', 'code', 'quantity', 'category', 'brand',
                    'cost_month', 'cost_week', 'cost_day', 'detail_url']
        return super(StockSerializer, self).get_field_names(declared_fields, info)

    def validate_rental(self, value):
        return [str(x) for x in value]
