from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# all_cars = ["bmw - очень крутая машина", "lada- сделано в СССР", "volvo - очень надежная машина"]
auto = Auto.objects.all()
context = {
        "cars": auto,
    }
def cars(request):
    return render(request, 'cars.html', context = context)

def bmw(request):
    bmw = Auto.objects.get(pk = 1)
    return render(request, 'bmw.html', {"bmw":bmw})

def lada(request):
    return render(request,'lada.html')

def volvo(request):
    return render(request,'volvo.html')