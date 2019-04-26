from django.contrib import admin

from customer.models import Agent, Customer, ContactPerson, BillingAddress, ShippingAddress

# Register your models here.

@admin.register(Agent, Customer, ContactPerson, BillingAddress, ShippingAddress)
class CustomerAdmin(admin.ModelAdmin):
    pass

