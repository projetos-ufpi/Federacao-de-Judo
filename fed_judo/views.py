from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def sobre(request):
    return render (request, 'sobre.html')

def cadastro_usuario(request):
    return render (request, 'cadastro_usuario.html')

def eventos(request):
    return render (request, 'eventos.html')

def rankings(request):
    return render (request, 'rankings.html')

def administracao(request):
    return render (request, 'administracao.html')
