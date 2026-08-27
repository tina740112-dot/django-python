from django.shortcuts import render
from .models import temperature_db
from django.http import HttpResponse

def view_history_temperature(request):
    temperatures = temperature_db.objects.all().order_by('-timestamp')
    return render(request, 'view_history_temperature.html', {'temperatures': temperatures})
   #return HttpResponse("Hello, world. You're at the temperature index.")
  
# Create your views here.

