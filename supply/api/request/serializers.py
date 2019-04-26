from rest_framework import serializers

from supply.api.items.serializers import StockGroupModelSerializer
from supply.models.request import PurchaseRequest


class PurchaseRequestModelSerializer(serializers.ModelSerializer):  # todo urls
    create_lpo = serializers.HyperlinkedIdentityField("supply:request:purchase-request-create-purchase-order")
    detail_url = serializers.HyperlinkedIdentityField("supply:request:purchase-request-detail")
    email = serializers.HyperlinkedIdentityField("supply:request:purchase-request-email")
    download = serializers.HyperlinkedIdentityField("supply:request:purchase-request-download")
    item_group = StockGroupModelSerializer()

    class Meta:
        model = PurchaseRequest
        fields = ["vendor", "priority", "purchase_number", "date",  # "sales_order"
                  "item_group", "notes", "footer",
                  "detail_url", "create_lpo", "email", "download"]

    def get_field_names(self, declared_fields, info):
        if self.context["view"].action in ["list"]:
            return ["vendor", "priority", "purchase_number", "date",
                    "detail_url", "create_lpo", "email", "download"]
        elif self.context["view"].action in ["update", "partial_update"]:
            return ["vendor", "priority", "purchase_number", "date",  # "sales_order"
                    "notes", "footer"]
        return super(PurchaseRequestModelSerializer, self).get_field_names(declared_fields, info)

    def create(self, validated_data):
        item_group = validated_data.pop("item_group")
        stock_group = StockGroupModelSerializer().create(validated_data=item_group)
        validated_data.update(dict(item_group=stock_group))
        return PurchaseRequest.objects.create(**validated_data)
