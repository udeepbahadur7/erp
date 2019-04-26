from rest_framework import serializers

from supply.models.vendors import Vendor, Reminder


class VendorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

    def get_field_names(self, declared_fields, info):
        if self.context.get("minimal"):
            return ["name", "mobile", "address_street", "address_city", "address_state",
                    "address_country", "balance"]
        return super(VendorModelSerializer, self).get_field_names(declared_fields, info)


class ReminderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ["title", "date_time", "message"]

    def __init__(self, *args, **kwargs):
        self.vendor = kwargs.pop("vendor", None)
        super(ReminderModelSerializer, self).__init__(*args, **kwargs)

    def save(self, **kwargs):
        kwargs.update(vendor=self.vendor)
        return super(ReminderModelSerializer, self).save(**kwargs)
