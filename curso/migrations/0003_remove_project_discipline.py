# Generated by Django 4.0.6 on 2024-05-15 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_project_discipline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='discipline',
        ),
    ]