from django.shortcuts import render
from .models import Localizacao, Festival

def festivals_list(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'festivais/index.html', {'localizacoes': localizacoes})

def festival_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivais/festival.html', {'festival': festival})
