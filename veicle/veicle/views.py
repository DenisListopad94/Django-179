from django.http import HttpResponse
from django.shortcuts import render




def first_page(request):
    return HttpResponse("Hello Django")


def info(request):
    return HttpResponse("<h1>info about cars</h1>")



