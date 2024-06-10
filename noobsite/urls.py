from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view),
    path('index2/', views.index_view2),
    path('index3/', views.index_view3),
]