from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Numero telefónico', 'class': 'form-control'})
        }