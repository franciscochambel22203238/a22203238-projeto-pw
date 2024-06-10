from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm

def is_editor_bandas(user):
    return user.groups.filter(name='editor_bandas').exists()

def lista_bandas_view(request):
    bandas = Banda.objects.all()
    context = {'bandas': bandas, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/lista_bandas.html', context)

def lista_albuns_view(request):
    albuns = Album.objects.all()
    context = {'albuns': albuns, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/lista_albuns.html', context)

def lista_musicas_view(request):
    musicas = Musica.objects.all()
    context = {'musicas': musicas, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/lista_musicas.html', context)

def detalhes_banda_view(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    albuns = Album.objects.filter(banda=banda)
    context = {'banda': banda, 'albuns': albuns, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/detalhes_banda.html', context)

def detalhes_album_view(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    musicas = Musica.objects.filter(album=album)
    context = {'album': album, 'musicas': musicas, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/detalhes_album.html', context)

def detalhes_musica_view(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    context = {'musica': musica, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/detalhes_musica.html', context)

def album_page_view(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/album_page.html', context)

def musica_page_view(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    context = {'musica': musica, 'is_editor': is_editor_bandas(request.user)}
    return render(request, 'bandas/musica_page.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def nova_banda_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = BandaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:lista_bandas')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)


@login_required
@user_passes_test(is_editor_bandas)
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_banda', banda_id=banda.id)
    else:
        form = BandaForm(instance=banda)  # cria formulário com dados da instância banda

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:lista_bandas')

@login_required
@user_passes_test(is_editor_bandas)
def novo_album_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = AlbumForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:lista_albuns')

    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_page', album_id=album.id)
    else:
        form = AlbumForm(instance=album)  # cria formulário com dados da instância album

    context = {'form': form, 'album':album}
    return render(request, 'bandas/edita_album.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:lista_albuns')

@login_required
@user_passes_test(is_editor_bandas)
def nova_musica_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = MusicaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:lista_musicas')

    context = {'form': form}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musica_page', musica_id=musica.id)
    else:
        form = MusicaForm(instance=musica)  # cria formulário com dados da instância musica

    context = {'form': form, 'musica':musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:lista_musicas')






