from django.db import models
from projects.models import Project

class Manuscript(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField('Название рукописи', max_length=255)
    file = models.FileField('Файл рукописи', upload_to='manuscripts/')
    comment = models.TextField('Комментарий', blank=True, null=True)
    uploaded_at = models.DateTimeField('Дата загрузки', auto_now_add=True)

    def __str__(self):
        return self.title