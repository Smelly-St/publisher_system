from django.db import models
from accounts.models import UserProfile


class Author(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    full_name = models.CharField('ФИО', max_length=255)
    contact_info = models.TextField('Контактная информация', blank=True, null=True)
    contract = models.FileField('Договор', upload_to='contracts/', blank=True, null=True)

    def __str__(self):
        return self.full_name