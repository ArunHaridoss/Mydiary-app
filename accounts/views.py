from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib import messages

# Create your views here.
def register(request):
     
     if request.method == "POST":
          user = registerForm(request.POST)
          if user.is_valid():
            user.save()
            user_name = user.cleaned_data.get('username')
            messages.success(request,"Account was succesfully created for Username: "+ ""+ user_name +". Please login!!")
            print("accoutn was ceated")
            return redirect('register')
          else:
               messages.error(request,"Account was not created.Please check your details")
               print("acccount was not created")


     form = registerForm()
     context={'form':form}
     return render(request,'accounts/register.html',context)

