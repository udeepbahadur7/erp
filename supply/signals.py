from django.db.models import F
from django.db.models.aggregates import Sum


def calculate_sub_total(sender, instance, *args, **kwargs):
    assert sender._meta.model_name.lower() == "itemline"
    instance.stock_group.sub_total = instance.stock_group.itemlines.aggregate(sub_total=Sum(F("total")))["sub_total"]
    instance.stock_group.save()
