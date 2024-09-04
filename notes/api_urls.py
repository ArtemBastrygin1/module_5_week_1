from django.urls import path
from . import views_api  # отдельные представления для API
from .apps import NotesConfig

app_name = NotesConfig.name


urlpatterns = [
    path('admin/users/', views_api.UserListCreateAPIView.as_view(), name='user-list'),
    path('admin/users/<int:pk>/', views_api.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('notes/', views_api.NoteListCreateAPIView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views_api.NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),
]
