from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Note


class MoteURLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='user', password='pass')
        self.admin_user = get_user_model().objects.create_superuser(username='admin', password='pass')
        self.note = Note.objects.create(
            title='Test Note',
            description='Test Description',
            user=self.user
        )

    def test_notes_list_url(self):
        self.client.login(username='user', password='pass')

        response = self.client.get(reverse('notes:notes-list'))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_url(self):
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('notes:note-detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_admin_user_list_url(self):
        self.client.login(username='admin', password='pass')
        response = self.client.get(reverse('notes-api:user-list'))  # Пространство имен 'notes-api'
        self.assertEqual(response.status_code, 200)

    def test_non_admin_user_list_url(self):
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('notes-api:user-list'))  # Пространство имен 'notes-api'
        self.assertEqual(response.status_code, 403)  # Обычному пользователю доступ запрещен

    def test_no_logi_user(self):
        response = self.client.get(reverse('notes-api:note-list'))
        self.assertEqual(response.status_code, 403)
