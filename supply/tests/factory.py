import factory

from inventory.factory import StockFactory
from supply.models import ItemLine


class VendorFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'supply.Vendor'


class ItemLineFactory(factory.DjangoModelFactory):
    class Meta:
        model = ItemLine

    item = factory.SubFactory(StockFactory)
    quantity = factory.Iterator([1, 2])
    description = factory.Sequence(lambda n: "desc%d" % n)
    price = factory.Iterator([200, 300, 400])


class PurchaseRequestFactory(factory.DjangoModelFactory):
    class Meta:
        model = "supply.PurchaseRequest"

    vendor = factory.SubFactory(VendorFactory)
