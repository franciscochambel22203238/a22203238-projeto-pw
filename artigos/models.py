from django.db import models

class Autor(models.Model):
    user = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='artigos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.user} - {self.artigo.titulo}"

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.autor.user} - {self.artigo.titulo} - {self.valor}"