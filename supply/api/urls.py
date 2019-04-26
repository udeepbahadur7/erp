from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vendors/', include(("supply.api.vendors.urls", "supply.api.vendors"), namespace="vendor")),
    path('items/', include(("supply.api.items.urls", "supply.api.items"), namespace="items")),
    path('request/', include(("supply.api.request.urls", "supply.api.request"), namespace="request")),
]
