from django.shortcuts import render
from .models import Usuario

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
		return render(request,'cadastro_usuario',{'codigo':codigo})
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
