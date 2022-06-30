from django.shortcuts import render

from office.models import Company


def index(request):
    return render(request, 'office/index.html')
