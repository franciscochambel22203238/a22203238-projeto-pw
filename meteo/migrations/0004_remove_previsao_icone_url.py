# Generated by Django 4.0.6 on 2024-06-06 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meteo', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previsao',
            name='icone_url',
        ),
    ]