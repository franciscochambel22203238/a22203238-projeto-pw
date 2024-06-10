from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.lista_bandas_view, name='lista_bandas'), #lista bandas
    path('albuns', views.lista_albuns_view, name='lista_albuns'), #lista albuns
    path('musicas', views.lista_musicas_view, name='lista_musicas'), #lista musicas
    path('banda/<int:banda_id>/', views.detalhes_banda_view, name='detalhes_banda'),#editar e apagar bandas
    path('album/<int:album_id>/', views.detalhes_album_view, name='detalhes_album'), #pagina album (sem editar e apagar)
    path('musica/<int:musica_id>/', views.detalhes_musica_view, name='detalhes_musica'), #pagina musica (sem editar e apagar)
    path('album/<int:album_id>/detalhes/', views.album_page_view, name='album_page'), #editar e apagar album
    path('musica/<int:musica_id>/page/', views.musica_page_view, name='musica_page'), #editar e apagar musica
    path('banda/nova', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view,name="apaga_banda"),
    path('album/novo', views.novo_album_view, name="novo_album"),
    path('album/<int:album_id>/edita', views.edita_album_view,name="edita_album"),
    path('album/<int:album_id>/apaga', views.apaga_album_view,name="apaga_album"),
    path('musica/nova', views.nova_musica_view, name="nova_musica"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),
    path('musica/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),

]
