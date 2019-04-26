import factory


from .models import agent, customer, contact_person, billing_address, shipping_address
from supply.constants import CREDIT_STATUS


class AgentFactory(factory.Factory):
    class Meta:
        model = agent.Agent

    agent_name = factory.Faker('name')
    email = factory.Faker('email')
    phone_number = factory.Iterator([9849324652, 9818822421])
    fax_number = 656767659
    street = factory.Faker('address')
    city = factory.Faker('city')
    po_box = factory.Faker('word')
    country = factory.Faker('country')
    profile_picture = factory.django.ImageField(color='blue')


class CustomerFactory(factory.Factory):
    class Meta:
        model = customer.Customer

    agent = factory.SubFactory(AgentFactory)
    customer_name = factory.Faker('name')
    email = factory.Faker('email')
    mobile_number = factory.Iterator([9849324652, 9818822421])
    fax = 656767659
    website = factory.Faker('url')
    house_number = factory.Faker('sentence')
    street = factory.Faker('paragraph')
    city = factory.Faker('city')
    po_box = factory.Faker('word')
    country = factory.Faker('country')
    state = factory.Faker('word')
    picture = factory.django.ImageField(color='red')

    payment_options = factory.Iterator([0, 1, 2, 3, 4])
    credit_status = factory.Iterator([CREDIT_STATUS.hold_over, CREDIT_STATUS.notify_over, CREDIT_STATUS.always_halt])
    branch = factory.Faker('city')
    customer_status = factory.Iterator([0, 1])


class ContactPersonFactory(factory.Factory):
    class Meta:
        model = contact_person.ContactPerson

    customer = factory.SubFactory(CustomerFactory)
    name = factory.Faker('name')
    phone = factory.Faker('phone')
    email = factory.Faker('email')
    designation = factory.Iterator([
        'manager', 'salesman',
    ])
    details = factory.Faker('paragraph')


class BillingAddressFactory(factory.Factory):
    class Meta:
        model = billing_address.BillingAddress

    customer = factory.SubFactory(CustomerFactory)
    delivery_address = factory.Faker('city')


class ShippingAddressFactory(factory.Factory):
    class Meta:
        model = shipping_address.ShippingAddress

    customer = factory.SubFactory(CustomerFactory)
    delivery_address = factory.Faker('city')









