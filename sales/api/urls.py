
from django.urls import path, include

urlpatterns = [
    path('enquiry/', include(("sales.api.enquiry.urls", "sales.api.enquiry"), namespace="enquiry")),
]
