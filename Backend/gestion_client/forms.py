from django import forms
from .models import Client, Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['client', 'evenement', 'date_achat']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'telephone']
