from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *


class LoginUserPersonalizado(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña'  # TODO make inline with field
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuario', 'class':'form-input'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class':'form-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # this is required to display the help_texts

        self.fields['username'].label='Usuario'
        self.fields['password'].label='Contraseña'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username',css_class="login-input"),
            Field('password',css_class="login-input"),
            Submit('submit','Iniciar Sesión')
        )
