from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_page, name = 'cursos'), #lista cursos
    path('<int:curso_id>/', views.curso_page, name='curso'), #editar e apagar curso
    path('disciplinas', views.disciplinas_page, name = 'disciplinas'), #lista disciplinas
    path('<int:course_id>/<int:discipline_id>/', views.disciplina_page, name='disciplina'), #pagina disciplina (sem editar e apagar)
    path('disciplina/<int:discipline_id>/', views.disciplina_pagee, name='disciplina_page'), #editar e apagar disciplina
    path('projetos', views.projetos_page, name = 'projetos'), #lista projetos
    path('<int:course_id>/<int:discipline_id>/<int:project_id>/', views.projeto_page, name='projeto'), # pagina projeto (sem editar e apagar)
    path('projeto/<int:project_id>/', views.projeto_pagee, name='projeto_page'), # editar e apagar projeto
    path('areascientificas', views.areasCientificas_view, name = 'areasCientificas'), #lista areas cientificas
    path('professores', views.professores_view, name = 'professores'), #lista professores
    path('linguagensprogramacao', views.linguagensProgramacao_view, name = 'linguagensProgramacao'),#lista ling prog.
    path('curso/novo', views.novo_curso_view, name="novo_curso"),
    path('<int:curso_id>/edita', views.edita_curso_view,name="edita_curso"),
    path('<int:curso_id>/apaga', views.apaga_curso_view,name="apaga_curso"),
    path('disciplina/nova', views.nova_disciplina_view, name="nova_disciplina"),
    path('disciplina/<int:disciplina_id>/edita', views.edita_disciplina_view,name="edita_disciplina"),
    path('disciplina/<int:disciplina_id>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),
    path('projeto/novo', views.novo_projeto_view, name="novo_projeto"),
    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path('areacientifica/nova', views.nova_areaCientifica_view, name="nova_areaCientifica"),
    path('professor/novo', views.novo_professor_view, name="novo_professor"),
    path('linguagemprogramacao/nova', views.nova_linguagemProgramacao_view, name="nova_linguagemProgramacao"),
]