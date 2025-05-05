from django.shortcuts import render

# Create your views here.
# bookings/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bookings home page (test)")
