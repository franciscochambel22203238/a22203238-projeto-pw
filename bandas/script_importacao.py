import json
from bandas.models import Banda, Album, Musica

Banda.objects.all().delete()
Musica.objects.all().delete()
Album.objects.all().delete()

with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)

    for banda_dados in bandas['bands']:
        Banda.objects.create(
            nome = banda_dados['name'],
            foto = banda_dados['photo'],
            informacoes = banda_dados['info']
        )

with open('bandas/json/albums.json') as f:
    data = json.load(f)

    for album_data in data['albums']:

        titulo = album_data['titulo']
        ano_de_lancamento = album_data['ano_de_lancamento']
        nome_banda = album_data['banda']

        banda, _ = Banda.objects.get_or_create(nome=nome_banda)

        album = Album.objects.create(
            titulo=titulo,
            ano_de_lancamento=ano_de_lancamento,
            banda=banda
        )

        for musica_data in album_data['musicas']:
            nome_musica = musica_data['titulo']
            duracao = musica_data['duracao']
            spotify_link = musica_data['spotify_link']

            musica = Musica.objects.create(
                nome=nome_musica,
                duracao=duracao,
                album=album,
                spotify_link=spotify_link
            )