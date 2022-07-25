from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from office.forms import UserRegistrationForm
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


def invoice_details(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    contact = Contact.objects.get(pk=invoice.contact_id)
    company = Company.objects.get(pk=invoice.company_id)
    context = {
        'company': company,
        'contact': contact,
        'invoice': invoice
    }
    return render(request, 'office/invoice/invoice_detail.html', context=context)


class HomeView(ListView):
    model = 'default'
    template_name = 'office/home.html'
    context_object_name = 'default'


@method_decorator(login_required, name='dispatch')
class OfficeCreateView(CreateView):
    model = 'default'
    template_name = 'office/home.html'
    fields = []


@method_decorator(login_required, name='dispatch')
class OfficeUpdateView(UpdateView):
    model = 'default'
    template_name = 'office/home.html'
    fields = []


@method_decorator(login_required, name='dispatch')
class OfficeDeleteView(DeleteView):
    model = "default"
    template_name = 'default'
    context_object_name = "default"
    success_url = reverse_lazy("home")


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "users/signup.html", {"form": form})


def profile(request):
    return redirect("home")


