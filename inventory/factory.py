import factory

from inventory.models import Stock, Category


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "cat_name%d" % n)


class StockFactory(factory.DjangoModelFactory):
    class Meta:
        model = Stock

    name = factory.Sequence(lambda n: "name%d" % n)
    code = factory.Sequence(lambda n: "code%d%d" % (n, n + 1))
    quantity = factory.Sequence(lambda n: n * 2)
    category = factory.SubFactory(CategoryFactory)
    brand = factory.Sequence(lambda n: "brand%d" % n)
    rental = factory.Iterator([["0", "1"], ["2", "1"]])
    hours_rate = factory.Iterator([8, 9, 10])
    extra_charge_rate = factory.Iterator([20, 25, 28])
    unit_type = factory.Iterator([0, 1])
    cost_month = factory.Iterator([500, 600])
    cost_week = factory.Iterator([300, 400])
    cost_day = factory.Iterator([100, 150])
    serial = factory.Sequence(lambda n: "serial%d" % n)
    capacity = factory.Iterator([50, 60])
    components = factory.Sequence(lambda n: "components%d" % n)
    asset_value = factory.Iterator([1000, 1500])

    # item specification
    width = factory.Iterator([10, 15])
    height = factory.Iterator([30, 35])
    weight = factory.Iterator([40, 50])
