from django.contrib import admin
from django.urls import path, include
from festivais import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/', include('pwsite.urls')),
    path('novaapp/', include('novaapp.urls')),
    path('festivais/', views.festivals_list, name='festivais_list'),
    path('festival/<int:festival_id>/', views.festival_detail, name='festival_detail'),
    path('bandas/', include('bandas.urls')),
    path('artigos/', include('artigos.urls')),
    path('cursos/', include('curso.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('meteo/', include('meteo.urls')),
    path('', include('portfolio.urls')),
]
