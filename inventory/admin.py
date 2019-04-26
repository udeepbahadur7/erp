from django.contrib import admin

# Register your models here.
from .models import Stock, Category
@admin.register(Category, Stock)
class QuotationAdmin(admin.ModelAdmin):
    pass
