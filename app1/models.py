from django.db import models

class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    identificacao = models.CharField(max_length=50)

    def __str__(self):
        return f"Primeiro nome: {self.primeiro_nome} | Ultimo nome: {self.ultimo_nome} | Idade: {self.idade} | Identificação: {self.identificacao}"

class Aluno(models.Model):
    nome = models.CharField(max_length=50)

class Computador(models.Model):
    modelo = models.CharField(max_length=50)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    alunos = models.ManyToManyField(Aluno)

