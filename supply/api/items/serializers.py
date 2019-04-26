from rest_framework import serializers

from supply.models.items import ItemLine, StockGroup


class ItemLineModelSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField("supply:items:itemline-detail")

    class Meta:
        model = ItemLine
        fields = ["item", "quantity", "price", "total", "description", "detail_url"]
        extra_kwargs = dict(
            price=dict(required=False)
        )

    def save(self, **kwargs):
        if self.context["view"].action == "create":
            kwargs.update(dict(stock_group_id=self.context["group"]))
        return super(ItemLineModelSerializer, self).save(**kwargs)


class StockGroupModelSerializer(serializers.ModelSerializer):
    itemlines = ItemLineModelSerializer(many=True, required=True)

    class Meta:
        model = StockGroup
        fields = ["itemlines"]

    def validate_itemlines(self, value):
        if len(value) == 0:
            return
        return value

    def create(self, validated_data):
        itemlines = validated_data.pop('itemlines')
        instance = StockGroup.objects.create()
        for itemline in itemlines:
            itemline.update(dict(stock_group=instance))
            ItemLine.objects.create(**itemline)
        return instance
