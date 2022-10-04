from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

def form_comment(request):
    if request.method == 'POST':
        form = FormComment(request.POST)
        if form.is_valid():
            Form_model_comment.objects.create(**form.cleaned_data)
            return redirect("cars")
    else:
        form = FormComment()
    return render(request, 'form.html',{"form":form})

def provider(request):
    if request.method == 'POST':
        form = FormProvider(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cars")
    else:
        form = FormProvider()
    return render(request, 'provider.html',{"form":form})