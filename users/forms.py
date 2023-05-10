from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django.forms import (
    CharField,
    Form,
    EmailField,
    ValidationError
)

from users.models import User


class RegisterForm(BaseUserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password1')

class CustomAuthenticationForm(AuthenticationForm):
    username = EmailField(required=True)  # note that this field is actually email


class PasswordResetForm(Form):
    password1 = CharField(max_length=255, required=True)
    password2 = CharField(max_length=255, required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Your passwords do not match")
        return password2
