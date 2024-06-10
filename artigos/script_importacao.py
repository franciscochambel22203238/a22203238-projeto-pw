from artigos.models import Autor, Artigo, Comentario, Rating
import json

Autor.objects.all().delete()
Artigo.objects.all().delete()
Comentario.objects.all().delete()
Rating.objects.all().delete()

with open('artigos/json/autores.json') as arquivo:
        dados = json.load(arquivo)
        autores = dados['autores']
        for autor_data in autores:
            Autor.objects.create(
                user=autor_data['username'],
                bio=autor_data['bio']
            )


with open('artigos/json/artigos.json') as arquivo:
        dados = json.load(arquivo)
        artigos = dados['artigos']
        for artigo_data in artigos:

            autor, _ = Autor.objects.get_or_create(user = artigo_data['autor'])

            Artigo.objects.create(
                titulo=artigo_data['titulo'],
                conteudo=artigo_data['conteudo'],
                data_publicacao=artigo_data['data_publicacao'],
                autor=autor,
                imagem=artigo_data['imagem']
            )