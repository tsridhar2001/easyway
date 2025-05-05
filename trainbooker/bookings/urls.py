# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('express/', views.book_express_ticket, name='book_express'),
    path('success/', views.express_booking_success, name='booking_success'),
    path('local/', views.book_local_ticket, name='book_local'),
    path('platform/', views.book_platform_ticket, name='book_platform'),
]
