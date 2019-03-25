from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.fields.EmailField(required=True,help_text="Please enter some valid email")
    class Meta:
        fields = ['username', 'email', 'password1', 'password2']
        model  = User