from django.db import models



# Create your models here.
class Usuario(models.Model):
    cpf = models.IntegerField(max_length=15,unique=True,null=True)
    nome = models.TextField()
    idade = models.IntegerField()
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
    enredeco_academia = models.TextField()

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
