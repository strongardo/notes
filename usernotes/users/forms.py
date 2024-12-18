from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')
