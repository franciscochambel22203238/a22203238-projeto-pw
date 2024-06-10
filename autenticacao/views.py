from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('autenticacao:login')

    return render(request, 'autenticacao/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('portfolio:landing_page')
        else:
            render(request, 'autenticacao/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'autenticacao/login.html')

def logout_view(request):
    logout(request)
    return redirect('portfolio:landing_page')

def welcome_view(request):
    return render(request, 'autenticacao/user.html')

@login_required
def perfil_view(request):
    return render(request, 'autenticacao/perfil.html')