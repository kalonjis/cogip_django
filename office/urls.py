from django.urls import path, include, reverse_lazy

from office.models import Company, Contact, Invoice
from office.views import HomeView, OfficeDetailView, OfficeUpdateView, OfficeDeleteView, OfficeCreateView, contact_details


app_name = "office"


urlpatterns = [
    path('company/', HomeView.as_view(model=Company, template_name='office/company/company_home.html', context_object_name='companies'), name='company-home'),
    path('contact/', HomeView.as_view(model=Contact, template_name='office/contact/contact_home.html', context_object_name='contacts'), name='contact-home'),
    path('invoice/', HomeView.as_view(model=Invoice, template_name='office/invoice/invoice_home.html', context_object_name='invoices'), name='invoice-home'),
    path('company/<str:slug>/',
         OfficeDetailView.as_view(model=Company, template_name='office/company/company_detail.html', context_object_name='company'),
         name='company-detail'),
    path('contact/<str:slug>/', contact_details, name='contact-detail'),
    path('invoice/<str:pk>/',
         OfficeDetailView.as_view(model=Invoice, template_name='office/invoice/invoice_detail.html', context_object_name='invoice'),
         name='invoice-detail'),
    path('company-create/',
         OfficeCreateView.as_view(model=Company, template_name='office/company/company_create.html', fields=['name', 'vat_number', 'type', 'country']),
         name='company-create'),
    path('contact-create/',
         OfficeCreateView.as_view(model=Contact, template_name='office/contact/contact_create.html', fields=['firstname', 'lastname', 'phone', 'email', 'company']),
         name='contact-create'),
    path('invoice-create/',
         OfficeCreateView.as_view(model=Invoice, template_name='office/invoice/invoice_create.html', fields=['company', 'contact']),
         name='invoice-create'),
    path('company-edit/<str:slug>/',
         OfficeUpdateView.as_view(model=Company, template_name='office/company/company_edit.html', fields=['name', 'vat_number', 'type', 'country']),
         name='company-edit'),
    path('contact-edit/<str:slug>/',
         OfficeUpdateView.as_view(model=Contact, template_name='office/contact/contact_edit.html', fields=['firstname', 'lastname', 'phone', 'email', 'company']),
         name='contact-edit'),
    path('invoice-edit/<str:pk>/',
         OfficeUpdateView.as_view(model=Invoice, template_name='office/invoice/invoice_edit.html', fields=['company', 'contact']),
         name='invoice-edit'),
    path('company-delete/<str:slug>/',
         OfficeDeleteView.as_view(model=Company, template_name='office/company/company_confirm_delete.html', context_object_name='company', success_url=reverse_lazy('office:company-home')),
         name='company-delete'),
    path('contact-delete/<str:slug>/',
         OfficeDeleteView.as_view(model=Contact, template_name='office/contact/contact_confirm_delete.html', context_object_name='contact', success_url=reverse_lazy('office:contact-home')),
         name='contact-delete'),
    path('invoice-delete/<str:pk>/',
         OfficeDeleteView.as_view(model=Invoice, template_name='office/invoice/invoice_confirm_delete.html', context_object_name='invoice', success_url=reverse_lazy('office:invoice-home')),
         name='invoice-delete'),

]

