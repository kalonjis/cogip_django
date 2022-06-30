from django.shortcuts import render

from office.models import Company


def base(request):
    return render(request, 'office/base.html')
