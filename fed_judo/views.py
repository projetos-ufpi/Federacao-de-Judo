from django.shortcuts import render
from .models import Usuario, Evento

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm




# Create your views here.
def index(request):
    return render (request, 'index.html')

def sobre(request):
    return render (request, 'sobre.html')

#def cadastro_usuario(request):
#	usuario = Usuario()
#	if(request.method=='POST'):
		#if(request.POST.get('senha')==request.POST.get('comfirmaca_senha')):
		#	usuario.setNome(request.POST.get('nome'))
    	#	return render (request, 'cadastro_usuario.html')
 #   	return render (request, 'cadastro_usuario.html')
 #  	return render (request, 'cadastro_usuario.html',{})

def eventos(request):
    return render (request, 'eventos.html')

def rankings(request):
    return render (request, 'rankings.html')

def login(request):
    return render(request, 'login.html')

def cadastro_eventos(request):
    eventos = Evento()
    codigo = 0
    if(request.method == 'POST'):
        eventos.setNome_Evento(request.POST.get('nome'))
        eventos.setData_Inicio(request.POST.get('data_inicio'))
        eventos.setData_Fim(request.POST.get('data_fim'))
        eventos.setPremiacao(request.POST.get('premiacao'))
        eventos.save()
        codigo = 1
        return render (request, 'cadastro_eventos.html', {'codigo':codigo})
    return render(request, 'cadastro_eventos.html', {'codigo':codigo})


def administracao(request):
    return render (request, 'administracao.html')


def cadastro_usuario(request):
	usuario = Usuario()
	codigo = 0
	if(request.method == 'POST' and request.POST.get('senha') == request.POST.get('confirmacao_senha')):
		usuario.setNome(request.POST.get('nome'))
		usuario.setEndereco(request.POST.get('endereco'))
		usuario.setTelefone(request.POST.get('telefone'))
		usuario.setDatadeNascimento(request.POST.get('data_nascimento'))
		usuario.setCpf(request.POST.get('cpf'))
		usuario.setUsername(request.POST.get('login'))
		usuario.setPassword(request.POST.get('senha'))
		usuario.save()
		codigo = 1
		return render(request,'cadastro_usuario.html',{'codigo':codigo})
	elif(request.method == 'POST' and request.POST.get('senha') != request.POST.get('confirmacao_senha')):
		usuario.setNome(request.POST.get('nome'))
		usuario.setEndereco(request.POST.get('endereco'))
		usuario.setTelefone(request.POST.get('telefone'))
		usuario.setDatadeNascimento(request.POST.get('data_nascimento'))
		usuario.setCpf(request.POST.get('cpf'))
		usuario.setUsername(request.POST.get('login'))
		codigo = 2
		return render(request,'cadastro_usuario.html',{'nome':usuario.getNome(),'endereco':usuario.getEndereco(),'telefone':usuario.getTelefone(),'data_nascimento':usuario.getDatadeNasciento(),'cpf':usuario.getCpf(),'username':usuario.getUsername(),'codigo':codigo})
	return render(request,'cadastro_usuario.html',{'codigo':codigo})

    
def consulta(request):
	consulta = ColetaAgendada()
	codigo = 0
	if(request.method == 'POST'):
		codigo = 1
		consulta.setNome(request.POST.get('nomecompleto'))
		consulta.setRua(request.POST.get('rua'))
		consulta.setBairro(request.POST.get('bairro'))
		consulta.setNumero(request.POST.get('numero'))
		consulta.setTelefone(request.POST.get('telefone'))
		consulta.setEmail(request.POST.get('email'))
		consulta.setComplemento(request.POST.get('complemento'))
		consulta.save()
		return render(request,'paginas/consulta.html',{'codigo':codigo})
	return render(request,'paginas/consulta.html',{'codigo':codigo})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
