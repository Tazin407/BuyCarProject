from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email']
        labels={
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }