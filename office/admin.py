from django.contrib import admin

# Register your models here.
from office.models import Company, Contact, Invoice

admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Invoice)
