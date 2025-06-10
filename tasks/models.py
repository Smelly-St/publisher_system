from django.db import models
from projects.models import Project
from authors.models import Author

class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнена')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField('Задача', max_length=255, default='Новая задача')
    assignee = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель')
    due_date = models.DateField('Срок выполнения')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.title