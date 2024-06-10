from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banda',
            name='ano_de_formacao',
        ),
        migrations.RemoveField(
            model_name='banda',
            name='genero',
        ),
        migrations.AddField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='capas/'),
        ),
        migrations.AddField(
            model_name='album',
            name='spotify_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='banda',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='bandas/'),
        ),
        migrations.AddField(
            model_name='banda',
            name='informacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='spotify_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.CharField(max_length=10),
        ),
    ]
