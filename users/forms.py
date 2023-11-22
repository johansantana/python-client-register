from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

from .models import ModifiedUser

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'placeholder': 'Usuario', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña', 'class': 'form-control'}
    ))

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = ModifiedUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        placeholders = ('Nombre', 'Apellido', 'Usuario', 'Correo electrónico', 'Número de teléfono', 'Contraseña', 'Confirmar contraseña')

        for i, fieldname in enumerate(self.fields):
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
            self.fields[fieldname].widget.attrs['placeholder'] = placeholders[i]
