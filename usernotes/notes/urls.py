from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('notes/', permanent=True)),
    path('notes/', views.notes_page, name='notes'),
    path('add/', views.add, name='add'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
