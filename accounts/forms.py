from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerForm(UserCreationForm):
    check=forms.BooleanField()
    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password1','password2','check']
