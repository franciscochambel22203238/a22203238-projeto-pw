from django.contrib import admin

from .models import Cidade, Previsao, PrevisaoProximos5Dias

admin.site.register(Cidade)
admin.site.register(Previsao)
admin.site.register(PrevisaoProximos5Dias)