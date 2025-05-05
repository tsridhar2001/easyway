# bookings/forms.py

from django import forms
from .models import ExpressTicket, LocalTicket, PlatformTicket

class ExpressTicketForm(forms.ModelForm):
    class Meta:
        model = ExpressTicket
        fields = ['train_name', 'source', 'destination', 'travel_date', 'travel_class', 'passengers']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LocalTicketForm(forms.ModelForm):
    class Meta:
        model = LocalTicket
        fields = ['line_direction', 'travel_date', 'ticket_count']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PlatformTicketForm(forms.ModelForm):
    class Meta:
        model = PlatformTicket
        fields = ['ticket_count']