from django.db import models
from accounts.models import UserProfile


class Staff(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.CharField('Отдел', max_length=100, blank=True, null=True)
    position = models.CharField('Должность', max_length=100)

    def __str__(self):
        return f"{self.user_profile.user.username} — {self.position}"