# Generated by Django 5.2 on 2025-06-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Бюджет'),
        ),
    ]
