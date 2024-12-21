from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddNoteForm
from .models import Note


def notes_page(request):
    notes = {}

    if request.user.is_authenticated:
        notes = request.user.notes.all()

    return render(request, 'notes.html', context={'notes': notes})


def add(request):
    form = AddNoteForm()
    if request.method == 'POST':
        # Note.objects.create(
        #     user=request.user,
        #     title=request.POST.get('title'),
        #     pub_date=request.POST.get('pubdate'),
        #     text=request.POST.get('text')
        # )

        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Создаем объект, но не сохраняем его в базу
            note.user = request.user
            # note.pub_date = datetime.now()
            note.save()
            return redirect('notes')

    return render(request, 'add.html', context={'form': form})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('notes')
