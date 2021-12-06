from django.shortcuts import render,redirect
from .models import Notes
from .forms import notesForm
from accounts.forms import registerForm
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def home(request):
    forms = registerForm()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')

        if username and password:
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('notes')
            else:
                messages.error(request, "username or password is not correct. Please enter valid Login details")    
    return render (request,'diaryapp/home.html',{'form':forms})

def notes(request):
    
    notes = Notes.objects.filter(user = request.user)
    context = {'notes':notes}
    return render(request,"diaryapp/notes.html",context)

def createNotes(request):
    notes = notesForm()
    context = {'notes':notes}
    if request.method == "POST":
        note = notesForm(request.POST)
        if note.is_valid():
            note.instance.user = request.user
            note.save()
            return redirect('/notes/')
    return render(request,'diaryapp/create_note.html',context)

def updateNotes(request,pk):
    notes = Notes.objects.get(id= pk)
    noteform = notesForm(instance=notes)
    context = {'noteform':noteform}
    if request.method == "POST":
        note = notesForm(request.POST,instance=notes)
        if note.is_valid():
            note.save()
            return redirect('/notes/')
    return render(request,'diaryapp/update_note.html',context)

def deleteNotes(request,pk):
    notes = Notes.objects.get(id=pk)
    context = {'notes':notes}
    if request.method == "POST":
        notes.delete()
        return redirect('/notes/')
    return render(request,'diaryapp/delete_note.html',context)
