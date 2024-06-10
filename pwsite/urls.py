from django.urls import path
from . import views

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('index2/', views.index_view2, name='index2'),
    path('index3/', views.index_view3, name='index3'),
]