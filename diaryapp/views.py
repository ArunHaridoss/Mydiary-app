from django.shortcuts import render,redirect
from .models import Notes
from .forms import notesForm

# Create your views here.
def home(request):
    return render (request,'diaryapp/home.html')
def notes(request):
    notes = Notes.objects.all()
    context = {'notes':notes}
    return render(request,"diaryapp/notes.html",context)

def createNotes(request):
    notes = notesForm()
    context = {'notes':notes}
    if request.method == "POST":
        note = notesForm(request.POST)
        if note.is_valid():
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