# Generated by Django 5.0 on 2024-01-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
