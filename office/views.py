from django.shortcuts import render
from django.views.generic import ListView

from office.models import Company
from django.views import View


class HomeView(ListView):
    model = 'default'
    template_name = 'office/home.html'
    context_object_name = 'default'

