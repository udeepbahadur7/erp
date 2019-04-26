from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from supply.models import StockGroup
from supply.models.items import ItemLine
from supply.tests.factory import ItemLineFactory


class TestItemLineViewSet(APITestCase):
    """This test signifies how to directly interact with itemline
    in the purchase request"""

    @classmethod
    def setUpClass(cls):
        super(TestItemLineViewSet, cls).setUpClass()
        cls.stock_group = StockGroup.objects.create()
        cls.itemlines = ItemLineFactory.create_batch(2, stock_group=cls.stock_group)
        cls.instance = cls.itemlines[0]
        cls.stock = cls.instance.item
        cls.pk = cls.instance.pk
        cls.detail_url = reverse("supply:items:itemline-detail",
                                 kwargs=dict(pk=cls.pk))
        cls.list_url = reverse("supply:items:itemline-list",
                               kwargs=dict(group=cls.stock_group.pk))
        cls.client = APIClient()

    def setUp(self):
        self.data = dict(
            quantity=5,
            description="new desc"
        )
        self.create_data = dict(
            item=self.stock.id,
            quantity=5,
            price=100,
            description="new desc"
        )

    def test_001_valid_update_delete_itemline(self):
        # update
        self.assertNotEqual(self.instance.quantity, self.data["quantity"])
        response = self.client.patch(self.detail_url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["quantity"], self.data["quantity"])
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.quantity, self.data["quantity"])

        # now deletion
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertRaises(ItemLine.DoesNotExist, self.instance.refresh_from_db)

    def test_002_valid_create_itemline(self):
        # add to existing stock group
        old = self.stock_group.itemlines.count()
        response = self.client.post(self.list_url, self.create_data)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data["quantity"], self.create_data["quantity"])
        self.assertEqual(self.stock_group.itemlines.count(), old + 1)

    def test_003_permissions(self):
        self.fail()
