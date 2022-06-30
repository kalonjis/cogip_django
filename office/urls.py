from django.urls import path, include

from office.views import  base

urlpatterns = [
    path('', base, name='base')
]