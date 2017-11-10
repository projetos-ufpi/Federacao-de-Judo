from django.db import models



# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length=15)
    nome = models.TextField()
    idade = models.IntegerField()
    telefone = models.TextField()
    endereco = models.TextField()

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
