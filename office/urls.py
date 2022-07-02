from django.urls import path, include

from office.models import Company, Contact, Invoice
from office.views import HomeView, OfficeDetailView, OfficeUpdateView

app_name = "office"

urlpatterns = [
    path('company/', HomeView.as_view(model=Company, template_name='office/company/company_home.html', context_object_name='companies'), name='company-home'),
    path('contact/', HomeView.as_view(model=Contact, template_name='office/contact/contact_home.html', context_object_name='contacts'), name='contact-home'),
    path('invoice/', HomeView.as_view(model=Invoice, template_name='office/invoice/invoice_home.html', context_object_name='invoices'), name='invoice-home'),
    path('company/<str:slug>/',
         OfficeDetailView.as_view(model=Company, template_name='office/company/company_detail.html', context_object_name='company'),
         name='company-detail'),
    path('contact/<str:slug>/',
         OfficeDetailView.as_view(model=Contact, template_name='office/contact/contact_detail.html', context_object_name='contact'),
         name='contact-detail'),
    path('invoice/<str:pk>/',
         OfficeDetailView.as_view(model=Invoice, template_name='office/invoice/invoice_detail.html', context_object_name='invoice'),
         name='invoice-detail'),
    path('company-edit/<str:slug>/',
         OfficeUpdateView.as_view(model=Company, template_name='office/company/company_edit.html', fields=['name', 'vat_number', 'type', 'country']),
         name='company-edit'),
    path('contact-edit/<str:slug>/',
         OfficeUpdateView.as_view(model=Contact, template_name='office/contact/contact_edit.html', fields=['firstname', 'lastname', 'phone', 'email', 'company']),
         name='contact-edit'),

]
