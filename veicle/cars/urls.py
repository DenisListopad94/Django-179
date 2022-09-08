from django.urls import path
from .views import *

urlpatterns = [
    path('cars/', cars, name="cars"),
    path('bmw/', bmw, name = "bmw"),
    path('lada/',lada, name = "lada"),
    path('volvo/',volvo, name = "volvo")
]