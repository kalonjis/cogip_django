from django.shortcuts import render
from django.views.generic import ListView, DetailView

from office.models import Company, Contact, Invoice
from django.views import View


def home(request):
    companies = Company.objects.all()
    contacts = Contact.objects.all()
    invoices = Invoice.objects.all()
    context = {
        'companies': companies,
        'contacts': contacts,
        'invoices': invoices,
    }
    return render(request, 'office/home.html', context=context)


class HomeView(ListView):
    model = 'default'
    template_name = 'office/home.html'
    context_object_name = 'default'


class OfficeDetailView(DetailView):
    model = 'default'
    template_name = 'office/home.html'
    context_object_name = 'default'


