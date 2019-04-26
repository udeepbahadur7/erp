from django.test import TestCase
from rest_framework.test import APIRequestFactory

from inventory.factory import StockFactory
from supply.api.request.serializers import PurchaseRequestModelSerializer
from supply.models.items import StockGroup
from supply.tests.factory import VendorFactory, PurchaseRequestFactory, ItemLineFactory


class View:
    def __init__(self, action):
        self.action = action


class TestPurchaseRequestModelSerializer(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestPurchaseRequestModelSerializer, cls).setUpClass()
        rf = APIRequestFactory()
        cls.request = rf.get("/")
        cls.stock_group = StockGroup.objects.create()
        cls.itemlines = ItemLineFactory.create_batch(2, stock_group=cls.stock_group)
        cls.instances = PurchaseRequestFactory.create_batch(2, item_group=cls.stock_group)
        cls.list_fields = ["vendor", "priority", "purchase_number", "date", "detail_url"]
        cls.update_fields = ["vendor", "priority", "purchase_number",
                             "date", "notes", "footer"]

    def setUp(self):
        self.vendor = VendorFactory.create()
        self.stock1 = StockFactory.create()
        self.stock2 = StockFactory.create()
        self.itemline1_data = dict(
            item=self.stock1.id,
            quantity=2,
            description="new desc"
        )
        self.itemline2_data = dict(
            item=self.stock2.id,
            quantity=3,
            description="new2 desc"
        )
        self.data = {
            "vendor": self.vendor.id,
            "priority": 0,
            # "purchase_number": "",
            "date": "2018-10-10",
            "item_group": {
                "itemlines": [
                    self.itemline1_data,
                    self.itemline2_data
                ]
            },
            "notes": "note",
            "footer": "footer"
        }
        self.context = dict(
            view=View(action="create")
        )
        self.serializer = PurchaseRequestModelSerializer(
            data=self.data,
            context=self.context
        )

    def test_001_valid_create_serializer(self):
        self.assertTrue(self.serializer.is_valid(), self.serializer.errors)
        instance = self.serializer.save()
        self.assertIsNotNone(instance.item_group)
        self.assertEqual(instance.item_group.itemlines.count(), len(self.data["item_group"]["itemlines"]))

    def test_001_1_invalid_empty_itemlines(self):
        self.data["item_group"] = {}
        self.assertFalse(self.serializer.is_valid())
        self.assertIn("itemlines", self.serializer.errors["item_group"])

        self.data["item_group"]["itemlines"] = []
        self.assertFalse(self.serializer.is_valid())
        self.assertIn("itemlines", self.serializer.errors["item_group"])

    def test_002_serializer_fields(self):
        context = dict(
            view=View(action="list"),
            request=self.request
        )
        serializer = PurchaseRequestModelSerializer(
            instance=self.instances,
            context=context,
            many=True
        )
        self.assertCountEqual(serializer.data[0].keys(), self.list_fields)

    def test_003_update_serializer_fields(self):
        context = dict(
            view=View(action="update"),
            request=self.request
        )
        serializer = PurchaseRequestModelSerializer(
            instance=self.instances[0],
            context=context,
        )
        self.assertCountEqual([each for each in serializer.fields], self.update_fields)

    def test_004_update_group_itemline_url(self):
        context = dict(
            view=View(action="retrieve"),
            request=self.request
        )
        instance = self.instances[0]
        serializer = PurchaseRequestModelSerializer(
            instance=instance,
            context=context,
        )
        self.assertIn("detail_url", serializer.data["item_group"]["itemlines"][0])
