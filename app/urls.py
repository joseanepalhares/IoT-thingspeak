from .views import templates
#from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', templates),
]
