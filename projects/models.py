from django.db import models

# Статусы проектов
STATUS_CHOICES = (
    ('new', 'Новый'),
    ('in_progress', 'В работе'),
    ('completed', 'Завершён'),
)

class Project(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    
    # Новые поля
    budget = models.DecimalField('Бюджет', max_digits=10, decimal_places=2, default=0)
    manager = models.ForeignKey(
        'authors.Author',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Ответственный менеджер'
    )

    def __str__(self):
        return self.title


# ✅ Прикрепляем STATUS_CHOICES к классу
Project.STATUS_CHOICES = STATUS_CHOICES