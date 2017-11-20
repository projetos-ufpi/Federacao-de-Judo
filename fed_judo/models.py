from django.db import models




# Create your models here.
class Usuario(models.Model):
    cpf = models.IntegerField(unique=True,null=True)
    nome = models.TextField()
    idade = models.IntegerField(null=True)
    telefone = models.TextField()
    endereco = models.TextField()
    data_nascimento = models.DateTimeField(blank=True,null=True)
    username = models.CharField(max_length=50,unique=True,null=True)
    password = models.CharField(max_length=50,null=True)

    def getCpf(self):
        return self.cpf
    def setCpf(self, cpf=''):
        self.nome = cpf
    def getNome(self):
        return self.nome
    def setNome(self, nome=''):
        self.nome = nome
    def setTelefone(self,telefone=''):
        self.telefone = telefone
    def getTelefone(self):
        return self.telefone
    def getEndereco(self):
        return self.endereco
    def setEndereco(self,endereco=''):
        self.endereco=endereco
    def getDatadeNasciento(self):
        return self.data_nascimento
    def setDatadeNascimento(self,data_nascimento=''):
        self.data_nascimento=data_nascimento;

    def getUsername(self):
        return self.username
    def setUsername(self,username=''):
        self.username=username
    def getPassword(self):
        return self.password
    def setPassword(self,password=''):
        self.password = password

class Academia(models.Model):
    id_academia = models.IntegerField()
    nome_Academia = models.TextField()
    endereco_academia = models.TextField()
    limite_atletas = models.IntegerField(null=True)

    def setIdAcademia(self, id_academia=''):
        self.id_academia = id_academia
    def getIdAcademia(self):
        return self.id_academia

    def setNomeAcademia(self, nome_Academia=''):
        self.nome_Academia = nome_Academia
    def getNomeAcademia(self):
        return self.nome_Academia

    def setEnderecoAcademia(self, endereco_academia=''):
        self.endereco_academia = endereco_academia
    def getEnderecoAcademia(self):
        return self.endereco_academia

    def setLimiteAtletasAcademia(self, limite_atletas=''):
        self.limite_atletas = limite_atletas
    def getLimiteAtletasAcademia(self):
        return self.limite_atletas




class Atleta(models.Model):
    academia_Associada = models.ForeignKey(Academia)
    categoria = models.TextField()
    graduacao = models.TextField()

class Administrador(models.Model):
    carga_horaria = models.IntegerField()
    salario = models.FloatField()


class Juiz(models.Model):
    posicao = models.TextField()
    funcao = models.TextField()

class Evento(models.Model):
    nome_evento = models.TextField()
    data_inicio = models.DateTimeField(blank=True,null=True)
    data_fim = models.DateTimeField(blank=True,null=True)
    premiacao = models.TextField()

    def setNome_Evento(self, nome_evento=''):
        self.nome_evento = nome_evento
    def getNome_Evento(self):
        return self.nome_evento

    def setData_Inicio(self, data_inicio=''):
        self.data_inicio = data_inicio
    def getData_Inicio(self):
        return self.data_inicio

    def setData_Fim(self, data_fim=''):
        self.data_fim = data_fim
    def getData_Fim(self):
        return self.data_fim

    def setPremiacao(self, premiacao=''):
        self.premiacao = premiacao
    def getPremiacao(self):
        return self.premiacao


class FaleConosco(models.Model):
    nome = models.TextField()
    email = models.TextField()
    mensagem = models.TextField()
    hora_envio = models.DateTimeField(blank=True,null=True)

    def setNome(self, nome=''):
        self.nome = nome
    def getNome(self):
        return self.nome

    def setEmail(self, email=''):
        self.email = email
    def getEmail(self):
        return self.email

    def setMensagem(self, mensagem=''):
        self.mensagem = mensagem
    def getMensagem(self):
        return self.mensagem

    def setHoraEnvio(self, hora_envio=''):
        self.hora_envio = hora_envio
    def getHotaEnvio(self):
        return self.hora_envio
