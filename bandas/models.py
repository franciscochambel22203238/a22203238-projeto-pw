from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas/', null=True, blank=True)
    informacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    ano_de_lancamento = models.IntegerField()
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    spotify_link = models.URLField(blank=True, null=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=10)
    spotify_link = models.URLField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.nome
