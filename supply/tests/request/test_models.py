from django.test import TestCase

from supply.models import StockGroup
from supply.models.request import PurchaseRequest
from supply.tests.factory import VendorFactory


class TestPurchaseRequestModel(TestCase):
    def setUp(self):
        self.fields = ["id", "priority", "purchase_number",
                       "date", "sales_order", "item_group", "notes",
                       "footer", "vendor"]
        self.vendor = VendorFactory.create()
        self.stock_group = StockGroup.objects.create()
        self.data = dict(
            vendor=self.vendor,
            item_group=self.stock_group,
        )

    def test_001_model_fields(self):
        actual_fields = [each.name for each in PurchaseRequest._meta.fields]
        self.assertCountEqual(actual_fields, self.fields)

    def test_002_auto_generated_purchase_number_if_blank(self):
        pr = PurchaseRequest(**self.data)
        pr.save()
        self.assertTrue(pr.purchase_number)

    def test_003_sales_order_foreign_key(self):
        self.fail()

    def test_004_items_populated_from_sales_order_if_chosen(self):
        self.fail()

    def test_005_purchase_request_send_mass_emails(self):
        self.fail()

    def test_006_purchase_request_send_vendor_email(self):
        self.fail()

    def test_007_update_instance_populates_history(self):
        pr = PurchaseRequest(**self.data)
        pr.save()
        self.assertEqual(pr.history.count(), 1)
        pr.purchase_number = "new number"
        pr.save()
        self.assertEqual(pr.history.count(), 2)
