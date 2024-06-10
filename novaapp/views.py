from django.shortcuts import render

def sport_view(request):
    return render(request, "novaapp/sport.html")

def lisboa_view(request):
    return render(request, "novaapp/lisboa.html")

def benfica_view(request):
    return render(request, "novaapp/benfica.html")