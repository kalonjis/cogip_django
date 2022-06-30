from django.shortcuts import render

from office.models import Company
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'office/home.html')


