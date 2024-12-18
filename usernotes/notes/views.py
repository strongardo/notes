from django.shortcuts import render


def notes_page(request):
    return render(request, 'notes.html')


def add_page(request):
    return render(request, 'add.html')
