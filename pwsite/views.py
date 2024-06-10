from django.shortcuts import render
from datetime import datetime


data_atual = datetime.now().strftime('%Y-%m-%d')
contexto = {'data': data_atual}

def index_view(request):
    return render(request, "pwsite/index.html", contexto)

def index_view2(request):
    return render(request, "pwsite/sobre.html", contexto)

def index_view3(request):
    return render(request, "pwsite/interesses.html", contexto)
