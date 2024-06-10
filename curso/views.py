from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Course, Discipline, Project, ScientificArea, Teacher, ProgrammingLanguage
from .forms import  CourseForm, DisciplineForm, ProjectForm, ScientificAreaForm, TeacherForm, ProgrammingLanguageForm

def is_editor_curso(user):
    return user.groups.filter(name='editor_curso').exists()

def cursos_page(request):
    cursos = Course.objects.all()
    return render(request, 'curso/cursos.html', { 'cursos' : cursos, 'is_editor': is_editor_curso(request.user)})

def curso_page(request, curso_id):
    curso = Course.objects.get(pk=curso_id)
    disciplinas = curso.disciplines.all()
    return render(request, 'curso/curso.html', {'curso': curso, 'disciplinas': disciplinas, 'is_editor': is_editor_curso(request.user)})

def disciplinas_page(request):
    disciplinas = Discipline.objects.all()
    return render(request, 'curso/disciplinas.html', { 'disciplinas' : disciplinas, 'is_editor': is_editor_curso(request.user)})

def disciplina_page(request, course_id, discipline_id):
    curso = Course.objects.get(pk=course_id)
    disciplina = Discipline.objects.get(pk=discipline_id)
    return render(request, 'curso/disciplina.html', {'disciplina': disciplina, 'curso': curso, 'is_editor': is_editor_curso(request.user)})

def disciplina_pagee(request, discipline_id):
    disciplina = Discipline.objects.get(pk=discipline_id)
    return render(request, 'curso/disciplina_page.html', {'disciplina': disciplina, 'is_editor': is_editor_curso(request.user)})

def projetos_page(request):
    projetos = Project.objects.all()
    return render(request, 'curso/projetos.html', { 'projetos' : projetos, 'is_editor': is_editor_curso(request.user) })

def projeto_page(request, course_id, discipline_id, project_id):
    curso = Course.objects.get(pk=course_id)
    projeto = Project.objects.get(pk=project_id)
    disciplina = Discipline.objects.get(pk=discipline_id)
    return render(request, 'curso/projeto.html', {'curso': curso, 'disciplina': disciplina, 'projeto' : projeto, 'is_editor': is_editor_curso(request.user)})

def projeto_pagee(request, project_id):
    projeto = Project.objects.get(pk=project_id)
    return render(request, 'curso/projeto_page.html', {'projeto' : projeto, 'is_editor': is_editor_curso(request.user)})

def areasCientificas_view(request):
    areasCientificas = ScientificArea.objects.all()
    return render(request, 'curso/areasCientificas.html', { 'areasCientificas' : areasCientificas, 'is_editor': is_editor_curso(request.user) })

def professores_view(request):
    professores = Teacher.objects.all()
    return render(request, 'curso/professores.html', { 'professores' : professores, 'is_editor': is_editor_curso(request.user) })

def linguagensProgramacao_view(request):
    linguagensProgramacao = ProgrammingLanguage.objects.all()
    return render(request, 'curso/linguagensProgramacao.html', { 'linguagensProgramacao' : linguagensProgramacao, 'is_editor': is_editor_curso(request.user) })

@login_required
@user_passes_test(is_editor_curso)
def novo_curso_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = CourseForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('cursos')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_curso_view(request, curso_id):
    curso = Course.objects.get(id=curso_id)

    if request.POST:
        form = CourseForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso', curso_id=curso.id)
    else:
        form = CourseForm(instance=curso)  # cria formulário com dados da instância curso

    context = {'form': form, 'curso':curso}
    return render(request, 'curso/edita_curso.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_curso_view(request, curso_id):
    curso = Course.objects.get(id=curso_id)
    curso.delete()
    return redirect('cursos')

@login_required
@user_passes_test(is_editor_curso)
def nova_disciplina_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = DisciplineForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('disciplinas')

    context = {'form': form}
    return render(request, 'curso/nova_disciplina.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_disciplina_view(request, disciplina_id):
    disciplina = Discipline.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplineForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('disciplina_page', discipline_id=disciplina.id)
    else:
        form = DisciplineForm(instance=disciplina)  # cria formulário com dados da instância disciplina

    context = {'form': form, 'disciplina':disciplina}
    return render(request, 'curso/edita_disciplina.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Discipline.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('disciplinas')

@login_required
@user_passes_test(is_editor_curso)
def novo_projeto_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ProjectForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('projetos')

    context = {'form': form}
    return render(request, 'curso/novo_projeto.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_projeto_view(request, projeto_id):
    projeto = Project.objects.get(id=projeto_id)

    if request.POST:
        form = ProjectForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto_page', project_id=projeto.id)
    else:
        form = ProjectForm(instance=projeto)  # cria formulário com dados da instância projeto

    context = {'form': form, 'projeto':projeto}
    return render(request, 'curso/edita_projeto.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_projeto_view(request, projeto_id):
    projeto = Project.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('projetos')

@login_required
@user_passes_test(is_editor_curso)
def nova_areaCientifica_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ScientificAreaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('areasCientificas')

    context = {'form': form}
    return render(request, 'curso/nova_areaCientifica.html', context)

@login_required
@user_passes_test(is_editor_curso)
def novo_professor_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = TeacherForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('professores')

    context = {'form': form}
    return render(request, 'curso/novo_professor.html', context)

@login_required
@user_passes_test(is_editor_curso)
def nova_linguagemProgramacao_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ProgrammingLanguageForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('linguagensProgramacao')

    context = {'form': form}
    return render(request, 'curso/nova_linguagemProgramacao.html', context)





