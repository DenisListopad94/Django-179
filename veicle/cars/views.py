from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
all_cars = ["bmw - очень крутая машина", "lada- сделано в СССР", "volvo - очень надежная машина"]

def cars(request):
    return render(request, 'cars.html', {"cars": all_cars})

def bmw(request):
    return render(request, 'bmw.html', {"bmw": "очень крутая машина"})

def lada(request):
    return render(request,'lada.html')

def volvo(request):
    return render(request,'volvo.html')