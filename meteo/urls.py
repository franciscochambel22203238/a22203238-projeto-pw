from django.urls import path
from . import views

urlpatterns = [
    path('previsao-lisboa/', views.previsao_lisboa, name='previsao_lisboa'),
    path('previsao-tempo/', views.previsao_tempo, name='previsao_tempo'),

    path('api/cidades', views.lista_cidades, name='lista_cidades'), #API
    path('api/previsao/hoje/<str:cidade_nome>', views.previsao_hoje, name='previsao_hoje'), #API
    path('api/previsao/proximos_5_dias/<str:cidade_nome>', views.previsao_proximos_5_dias, name='previsao_proximos_5_dias') #API
]