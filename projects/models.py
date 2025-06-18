from django.db import models
from accounts.models import UserProfile


class Project(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершён')
    )

    title = models.CharField('Название проекта', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    status = models.CharField('Статус', max_length=50, choices=STATUS_CHOICES, default='new')
    budget = models.DecimalField('Бюджет проекта', max_digits=10, decimal_places=2, default=0.00)
    manager = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='authored_projects')
    manuscript = models.FileField('Рукопись', upload_to='manuscripts/', null=True, blank=True)

    def __str__(self):
        return self.title