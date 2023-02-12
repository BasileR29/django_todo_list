from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

from . import forms, models

@login_required
def home(request):
    notes = models.Note.objects.filter(is_public=True)
    
    privees = models.Note.objects.filter(auteur=request.user)
    return render(request, 'todo/home.html', {'notes':notes, 'privees':privees})


@login_required
def create_note(request):
    form = forms.NoteForm()
    
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        
        if form.is_valid():
            
            note = form.save(commit=False)
            note.auteur = request.user
            note.save()
            
            return redirect("home")
    
    return render(request, "todo/create_note.html", {'form':form})

@login_required
def delete_note(request, note_id):
    note = models.Note.objects.get(pk=note_id)
    note.delete()
    
    return redirect("home")

@login_required
def edit_note(request, note_id):
    
    note = get_object_or_404(models.Note, id=note_id)
    edit_form = forms.NoteForm(instance=note)
    
    if request.method =='POST':
        edit_form = forms.NoteForm(request.POST, instance=note)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    
    return render(request, "todo/edit_note.html", {'form':edit_form})