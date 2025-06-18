from django.db import models

class StaticPage(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', unique=True)
    content = models.TextField('Контент')
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title