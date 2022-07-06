from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


def company_details(request, slug):
    company = Company.objects.get(slug=slug)
    contacts = Contact.objects.filter(company_id=company.id)
    invoices = Invoice.objects.filter(company_id=company.id)
    context = {
        'company': company,
        'contacts': contacts,
        'invoices': invoices
    }
    return render(request, 'office/company/company_detail.html', context=context)


def contact_details(request, slug):
    contact = Contact.objects.get(slug=slug)
    invoices = Invoice.objects.filter(contact_id=contact.id)
    context = {
        'contact': contact,
        'invoices': invoices,
    }
    return render(request, 'office/contact/contact_detail.html', context=context)


class HomeView(ListView):
    model = 'default'
    template_name = 'office/home.html'
    context_object_name = 'default'


class OfficeDetailView(DetailView):
    model = 'default'
    template_name = 'office/home.html'
    context_object_name = 'default'


class OfficeCreateView(CreateView):
    model = 'default'
    template_name = 'office/home.html'
    fields = []

class OfficeUpdateView(UpdateView):
    model = 'default'
    template_name = 'office/home.html'
    fields = []


class OfficeDeleteView(DeleteView):
    model = "default"
    template_name = 'default'
    context_object_name = "default"
    success_url = reverse_lazy("home")


