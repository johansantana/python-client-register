from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']
        labels = {
            'first_name': '', 
            'last_name': '', 
            'username': '', 
            'email': '',
            'phone_number': '', }