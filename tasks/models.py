# tasks/models.py

from django.db import models
from accounts.models import UserProfile
from projects.models import Project


class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнена')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assignees = models.ManyToManyField(UserProfile, related_name='assigned_tasks', verbose_name='Исполнители')
    due_date = models.DateField('Срок выполнения')
    status = models.CharField('Статус', max_length=50, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.title