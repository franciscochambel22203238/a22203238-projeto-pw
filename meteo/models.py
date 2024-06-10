from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Previsao(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data = models.DateField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    descricao_tempo = models.CharField(max_length=255)
    precipitacao = models.FloatField()

    def __str__(self):
        return self.cidade.id

class PrevisaoProximos5Dias(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data = models.DateField()
    temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    descricao_tempo = models.CharField(max_length=100)
    precipitacao = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Previsões para {self.cidade.nome}"