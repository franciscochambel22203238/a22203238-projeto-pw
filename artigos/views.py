from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Artigo, Autor, Rating, Comentario
from .forms import ArtigoForm, AutorForm, ComentarioForm, RatingForm
from django.db.models import Avg

def is_editor_artigos(user):
    return user.groups.filter(name='editor_artigos').exists()

def lista_artigos_view(request):
    artigos = Artigo.objects.all()
    context = {'artigos': artigos, 'is_editor': is_editor_artigos(request.user)}
    return render(request, 'artigos/lista_artigos.html', context)

def lista_autores_view(request):
    autores = Autor.objects.all()
    context = {'autores': autores, 'is_editor': is_editor_artigos(request.user)}
    return render(request, 'artigos/lista_autores.html', context)

def autor_page_view(request, autor_id, artigo_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    context = {'autor': autor, 'artigo' : artigo, 'is_editor': is_editor_artigos(request.user)}
    return render(request, 'artigos/autor_page.html', context)

def artigo_details_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo).order_by('-data_comentario')
    avaliacoes = Rating.objects.filter(artigo=artigo)

    if avaliacoes.exists(): #média
        media_avaliacoes = avaliacoes.aggregate(Avg('valor'))['valor__avg']
    else:
        media_avaliacoes = None

    context = {'artigo': artigo, 'is_editor': is_editor_artigos(request.user), 'comentarios': comentarios, 'avaliacoes': avaliacoes, 'media_avaliacoes': media_avaliacoes}
    return render(request, 'artigos/artigo_details.html', context)

def autor_details_view(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    context = {'autor': autor, 'is_editor': is_editor_artigos(request.user)}
    return render(request, 'artigos/autor_details.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def novo_artigo_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ArtigoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos')

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)  # cria formulário com dados da instância artigo

    context = {'form': form, 'artigo':artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('artigos:lista_artigos')

@login_required
@user_passes_test(is_editor_artigos)
def novo_autor_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = AutorForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)

    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_autor', autor_id=autor.id)
    else:
        form = AutorForm(instance=autor)  # cria formulário com dados da instância autor

    context = {'form': form, 'autor':autor}
    return render(request, 'artigos/edita_autor.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('artigos:lista_autores')

@login_required
@user_passes_test(is_editor_artigos)
def novo_comentario_view(request, artigo_id):

    artigo = get_object_or_404(Artigo, pk=artigo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.save()
            return redirect('artigos:detalhes_artigo', artigo_id=artigo.id)
    else:
        form = ComentarioForm()

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/novo_coment.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def novo_rating_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.artigo = artigo
            rating.save()
            return redirect('artigos:detalhes_artigo', artigo_id=artigo.id)
    else:
        form = RatingForm()

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/novo_rating.html', context)




