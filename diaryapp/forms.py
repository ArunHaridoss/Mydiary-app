from django import forms
from django.forms import ModelForm
from .models import Notes
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class notesForm(ModelForm):
    class Meta:
        model = Notes
        fields ="__all__"

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your E-mail address"}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Nmae'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter your password'}))
    check = forms.BooleanField()

    class Meta:
        model = User
        fields = "__all__"

