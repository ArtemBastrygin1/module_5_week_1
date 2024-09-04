from django.urls import path
from . import views  # представления для веб-шаблонов
from .apps import NotesConfig

app_name = NotesConfig.name

urlpatterns = [
    path('', views.notes_list, name='notes-list'),
    path('<int:pk>/', views.note_detail, name='note-detail'),
]
