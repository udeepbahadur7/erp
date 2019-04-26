from django.core.validators import MinValueValidator
from django.db import models
from multiselectfield import MultiSelectField
from six import python_2_unicode_compatible

from inventory.constants import UNIT
from inventory.exceptions import OutOfStock
from inventory.utils import stock_image_path
from libs.constants import RENTAL_CHOICES


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField("Name", max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Stock(models.Model):
    UNIT_CHOICES = (
        (UNIT.pcs, "pcs"),
        (UNIT.nos, "nos"),
    )

    name = models.CharField("Name", max_length=256)
    code = models.CharField("SKU", max_length=32)
    quantity = models.PositiveIntegerField("Current Quantity", blank=False, default=0)
    category = models.ForeignKey("inventory.Category", on_delete=models.SET_NULL,
                                 null=True)
    brand = models.CharField("Brand", max_length=128)
    image = models.ImageField("Picture", upload_to=stock_image_path)
    rental = MultiSelectField("Rental Type", choices=RENTAL_CHOICES)
    hours_rate = models.PositiveIntegerField("Hours per Day", default=24,
                                             blank=True,
                                             help_text="Limit of usage of this stock hours per day.")
    extra_charge_rate = models.FloatField("Extra Hours Charge Rate", default=0,
                                          blank=True,
                                          help_text="Extra Charge for overuse of this stock")
    unit_type = models.PositiveSmallIntegerField("Unit Type", choices=UNIT_CHOICES)
    cost_month = models.FloatField("Cost per Month", blank=True, null=True)
    cost_week = models.FloatField("Cost per Week", blank=True, null=True)
    cost_day = models.FloatField("Cost per Day", blank=True, null=True)
    serial = models.CharField("Serial Number", max_length=64)
    capacity = models.FloatField("Capacity", blank=True, null=True)
    components = models.TextField("Components")
    asset_value = models.FloatField("Asset Value",
                                    blank=True, null=True,
                                    validators=[MinValueValidator(1, "Add value greater than 1.")])

    # item specification
    width = models.FloatField("Size: width", blank=True, null=True)
    height = models.FloatField("Size: height", blank=True, null=True)
    weight = models.FloatField("Weight/Mass", blank=True, null=True)

    # stock history attributes: calculated on purchases
    last_purchase_amount = models.FloatField("Last Purchase Amount",
                                             blank=True, null=True)
    average_amount = models.FloatField("Average Amount",
                                       blank=True, null=True)

    def reduce_quantity(self, by=1):
        self.quantity -= by
        if self.quantity < 0:
            raise OutOfStock("Items stock is inadequate.")
        self.save()

    def increase_quantity(self, by=1):
        self.quantity += by
        self.save()

    def save(self, *args, **kwargs):
        self.last_purchase_amount = 0  # todo
        self.average_amount = 0
        return super(Stock, self).save(*args, **kwargs)
