from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerForm(UserCreationForm):
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter your password'}))
    check=forms.BooleanField()
    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password1','password2','check']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your E-mail address'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Userame'})
        }

        def clean_username(self):
            username = self.cleaned_data['username']
            if(len(username)<2):
                raise forms.ValidationError("username length should be minimum 3")
            return username
