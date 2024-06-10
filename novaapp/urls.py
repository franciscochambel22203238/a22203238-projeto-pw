from django.urls import path
from . import views

app_name = 'novaapp'

urlpatterns = [
    path('sport/', views.sport_view, name='sport'),
    path('lisboa/', views.lisboa_view, name='lisboa'),
    path('benfica/', views.benfica_view, name='benfica'),
]