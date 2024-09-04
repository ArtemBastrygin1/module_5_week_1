from django.db import models
from django.contrib.auth import get_user_model

NULLABLE = {
    'blank': True,
    'null': True
}


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        db_table = 'notes'

    def __str__(self):
        return self.title
