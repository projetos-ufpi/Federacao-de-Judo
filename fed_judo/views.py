from django.shortcuts import render
from .models import Usuario, Evento, FaleConosco, Academia, Noticia

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from datetime import datetime

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

from random import randint


def academias(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    academias = Academia.objects.all()#.order_by('published_date')
    return render (request, 'academias.html', {'academias':academias})


<<<<<<< HEAD

=======
56
>>>>>>> 266fb7ca451a03d65eda446e8e797fe3a8be4cc7
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
<<<<<<< HEAD
    eventos = Evento.objects.all()
    return render (request, 'eventos.html', {'eventos':eventos})
    
=======
    ns = Noticia.objects.all()
    eventos = Evento.objects.all()
    return render (request, 'eventos.html', {'eventos':eventos, 'ns':ns})

>>>>>>> 266fb7ca451a03d65eda446e8e797fe3a8be4cc7

def rankings(request):
    academias = Academia.objects.all().order_by('pontuacao')
    return render (request, 'rankings.html', {'academias':academias})



def login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')#'teste'# aqui e pego o que está no formulario html e salvo na var de ususario
        password = request.POST.get('senha')#'tomaz123'# aqui e pego o que está no formulario html e salvo na var de senha
        print(username)#isso é so um print comum
        user  = auth.authenticate(username=username, password=password)# essa função pronta do djanco para verificae e logar em uma conta
        if user is not None:
            auth.login(request, user)#aqui é sogado e construido a request com os dados de
            return HttpResponseRedirect('/index/')#tela de feeds chamada se der certo logui
            if request.user.is_authenticaded():
                return HttpResponseRedirect('/index/')
        else:
            #c = {}
            #c.update(csrf(request))
            #c.update({'error_message': 'Senha ou Usuario Incorretos'})
            return render(request, 'interface_usuario.html', {})# ususario e senhas invalidas arruamar a pagina para exibir erro
    return render (request, 'login.html')


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



def fale_conosco(request):
    mensagem = FaleConosco()
    codigo = 0
    if (request.method == 'POST'):
        mensagem.setNome(request.POST.get('nome'))
        mensagem.setEmail(request.POST.get('email'))
        mensagem.setMensagem(request.POST.get('mensagem'))
        mensagem.setHoraEnvio(datetime.now())
        mensagem.save()
        codigo = 1
        return render (request, 'fale_conosco.html', {'codigo':codigo})
    return render(request, 'fale_conosco.html', {'codigo':codigo})


def cadastro_academias(request):#corrigir a atribuição de id para academia/inserir pesquisa para verificar se o valor já está salvo no banco
    academia = Academia()
    codigo = 0
    if (request.method == 'POST'):
        academia.setNomeAcademia(request.POST.get('nome_Academia'))
        academia.setEnderecoAcademia(request.POST.get('endereco_academia'))
        academia.setLimiteAtletasAcademia(request.POST.get('limite-atletas'))
        academia.setTelefone(request.POST.get('telefone_academia'))
<<<<<<< HEAD
=======
        academia.setPontuacao(0)
        academia.setEmail(request.POST.get('email_academia'))
>>>>>>> 266fb7ca451a03d65eda446e8e797fe3a8be4cc7
        academia.setIdAcademia(randint(0, 9999999))
        academia.save()
        codigo = 1
        return render (request, 'cadastro_academias.html', {'codigo':codigo})

    return render(request, 'cadastro_academias.html', {'codigo': codigo})


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


def interface_usuario(request):
    return render (request, 'interface_usuario.html')


def informacoes_eventos(request):
    return render (request, 'informacoes_eventos.html')
