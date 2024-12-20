from django import forms
from .models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
