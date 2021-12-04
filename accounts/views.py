from django.shortcuts import render,redirect
from .forms import registerForm

# Create your views here.
def register(request):
     form = registerForm()
     context={'form':form}
     return render(request,'accounts/register.html',context)
