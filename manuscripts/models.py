# manuscripts/models.py

from django.db import models
from accounts.models import UserProfile
from projects.models import Project


class Manuscript(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='manuscripts')
    title = models.CharField('Название рукописи', max_length=255)
    file = models.FileField('Файл рукописи', upload_to='manuscripts/')
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='manuscripts')

    def __str__(self):
        return self.title