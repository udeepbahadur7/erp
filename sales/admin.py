from django.contrib import admin


from sales.models import Enquiry, Quotation
# Register your models here.
@admin.register(Enquiry, Quotation)
class SalesAdmin(admin.ModelAdmin):
    pass
