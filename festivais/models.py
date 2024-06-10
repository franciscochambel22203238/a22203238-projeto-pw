from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas = models.ManyToManyField(Banda)
    foto = models.ImageField(upload_to='festivals/', null=True, blank=True)

    def __str__(self):
        return self.nome
