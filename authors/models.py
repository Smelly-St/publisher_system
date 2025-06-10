from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    contact_info = models.TextField('Контакты', blank=True, null=True)

    # Поле user — связь с пользователем
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='author_profile'
    )

    def __str__(self):
        return self.full_name