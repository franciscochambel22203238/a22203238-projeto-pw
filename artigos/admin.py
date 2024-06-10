from django.contrib import admin
from .models import Autor, Artigo, Comentario, Rating

admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Rating)