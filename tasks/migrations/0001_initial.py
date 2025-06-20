# Generated by Django 5.2 on 2025-06-17 20:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Задача')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('due_date', models.DateField(verbose_name='Срок выполнения')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В работе'), ('completed', 'Выполнена')], default='new', max_length=50, verbose_name='Статус')),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Проект')),
            ],
        ),
    ]
