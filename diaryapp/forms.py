from django import forms
from django.forms import ModelForm
from .models import Notes

  
class notesForm(ModelForm):
    class Meta:
        model = Notes
        fields ="__all__"





        
    
