# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookings_home'),  # just a placeholder
]
