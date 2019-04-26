
from django.urls import path, include

urlpatterns = [
    path('agent/', include(("customer.api.agent.urls", "customer.api.agent"), namespace="agent")),
    path('contact_person/', include(("customer.api.contact_person.urls", "customer.api.contact_person"), namespace="contact_person")),
    path('billing_address/', include(('customer.api.billing_address.urls', 'customer.api.billing_address'), namespace='billing_address')),
    path('customer/', include(
        ('customer.api.customer.urls', 'customer.api.customer'),
        namespace='customer'
    ))
]
