from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('manager', 'Менеджер проекта'),
        ('author', 'Автор'),
        ('editor', 'Сотрудник издательства'),
        ('printer', 'Сотрудник типографии')
    )

    role = models.CharField('Роль', max_length=50, choices=ROLE_CHOICES, default='author')
    avatar = models.ImageField('Аватар', upload_to='avatars/', null=True, blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True, null=True)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.username