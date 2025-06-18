from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=UserProfile)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Ничего не делаем, если это новый пользователь
        pass

    # Не вызываем instance.save(), чтобы избежать рекурсии
    # Все поля уже сохранены через модель