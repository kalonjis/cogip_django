from django.urls import path, include

from office.models import Company, Contact, Invoice
from office.views import HomeView


urlpatterns = [
    path('company/', HomeView.as_view(model=Company, template_name='office/company_home.html', context_object_name='company-home')),
    path('contact/',
         HomeView.as_view(model=Contact, template_name='office/contact_home.html', context_object_name='contact-home')),
    path('invoice/',
         HomeView.as_view(model=Invoice, template_name='office/invoice_home.html', context_object_name='invoice-home')),

]