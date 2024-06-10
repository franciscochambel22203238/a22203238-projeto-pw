from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos_view, name='lista_artigos'), #lista artigos
    path('autores/', views.lista_autores_view, name='lista_autores'),#lista autores
    path('autor/<int:artigo_id>/<int:autor_id>/', views.autor_page_view, name='autor_page'),#pagina autor (sem editar e apagar)
    path('artigo/<int:artigo_id>/', views.artigo_details_view, name='detalhes_artigo'), #pagina de editar e apagar
    path('autor/<int:autor_id>/', views.autor_details_view, name='detalhes_autor'), #pagina de editar e apagar
    path('artigo/novo', views.novo_artigo_view, name="novo_artigo"),
    path('artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
    path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
    path('autor/novo', views.novo_autor_view, name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
    path('artigo/<artigo_id>/novo-comentario', views.novo_comentario_view, name="novo_comentario"),
    path('artigo/<artigo_id>/novo-rating', views.novo_rating_view, name="novo_rating"),
]