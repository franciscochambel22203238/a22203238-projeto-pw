from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('me-by-me', views.meByMe_view, name='mebyme'),
    path('apresentacao', views.apresentacao_view, name='apresentacao')
]