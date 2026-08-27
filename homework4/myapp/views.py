from django.shortcuts import render
from .models import temperature_db
from django.http import HttpResponse

def temperature(request):
    return HttpResponse("Hello, world. You're at the temperature index.")
  
# Create your views here.

