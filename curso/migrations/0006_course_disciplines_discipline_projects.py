# Generated by Django 4.0.6 on 2024-05-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_remove_course_disciplinas'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='disciplines',
            field=models.ManyToManyField(related_name='courses', to='curso.discipline'),
        ),
        migrations.AddField(
            model_name='discipline',
            name='projects',
            field=models.ManyToManyField(related_name='disciplines', to='curso.project'),
        ),
    ]
