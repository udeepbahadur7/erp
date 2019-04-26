"""ckgerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/supply/', include(
        ("supply.api.urls", "supply.api."),
        namespace="supply"
    )),
    path('v1/sales_customer/', include(
        ('customer.api.urls', 'customer.api.'),
        namespace='sales_customer'
    )),
    path('v1/sales/', include(
        ('sales.api.urls', 'sales.api'),
        namespace='sales'
    )),
    path('v1/inventory/', include(
        ('inventory.api.urls', 'inventory.api'),
        namespace='inventory'
    ))
]
