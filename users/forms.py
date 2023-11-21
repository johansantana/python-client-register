from django.contrib.auth.forms import UserCreationForm
from .models import ModifiedUser


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = ModifiedUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
