from django.db import models
from django.db.models import permalink
import datetime
from django.contrib.auth.models import User

# Create your models here.
# Informações sobre os modelos criados.

#ESPAÇOS PARA AS AÇÕES
# Aqui serão mostradas as ações já feitas por voluntários. Serão mostradas fotos do que foi feito, etc...
# Nome entidade, texto formatado e slider para fotos.

# Entidades de PF
# Lista de necessidades das entidades com fotos

# Voluntários
# Cadastro de volintários
# Nome completo, data de nascimento?, email, telefone, disponibilidade(Campo texto), vínculo à ONG

# SUPERUSER:
# theman
# iam

# class Voluntario(models.Model):
# 	"""Cadastro dos voluntários"""
# 	nome = models.CharField(max_length = 50)
# 	email = models.EmailField()
# 	telefone = models.CharField(max_length = 15)
# 	disponibilidade = models.TextField('Disponibilidade:')
# 	ong = models.TextField('Vinculo com ONGs:')

class Entidade(models.Model):
	"""Entidades e suas necessidades"""
	nome = models.CharField('Nome da entidade:', max_length = 50)
	url = models.SlugField(
		'URL',
		max_length=200,
		help_text = 'URL baseada no título',
		unique = True
		)
	imagemEntidade = models.ImageField(upload_to='entidade/%Y/%m/%d', null=True)
	site = models.URLField('Website da entidade:', blank = True)
	conteudo = models.TextField('Lista de necessidades:', default = '<ul> <li>Texto</li> </ul>')
	data = models.DateTimeField('Data de criação:', default=datetime.datetime.now)
	facebook =  models.URLField('Facebook:', blank = True)

	def __str__(self):
		return self.nome

class Acao(models.Model):
	"""docstring for Acao"""
	nome = models.CharField('Título:', max_length = 50)
	url = models.SlugField(
		'URL',
		max_length=200,
		help_text = 'URL baseada no título',
		unique = True)
	imagemAcao = models.ImageField(upload_to='acao/%Y/%m/%d', null=True)
	descricao = models.TextField('Descrição da(s) necessidade(s):')
	entidade = models.ManyToManyField(Entidade)
	situacao = models.BooleanField('Aberto/Fechado', 
		null = False, 
		default = False,
		help_text = 'Marque para dar a Ação como encerrada.'
		)
	data = models.DateTimeField('Data de criação:')

	def __str__(self):
		return self.nome

class Campanha(models.Model):
	nome = models.CharField('Título:', max_length = 50)
	url = models.SlugField(
		'URL',
		max_length=200,
		help_text = 'URL baseada no título',
		unique = True
		)
	imagemCampanha = models.ImageField(upload_to='campanha/%Y/%m/%d', null=True)
	descricao = models.TextField('Descrição da campanha:')
	data = models.DateTimeField('Data de criação:')
	facebook =  models.URLField(blank = True)

	def __str__(self):
		return self.nome

class Calendario(models.Model):
	"""docstring for Calendario"""

	nome = models.CharField('Nome da atividade:', max_length = 50)
	url = models.SlugField(
		'URL',
		max_length=200,
		help_text = 'URL baseada no título',
		unique = True
		)
	imagemCalendario = models.ImageField('900x300', upload_to='calendario/%Y/%m/%d', null=True)
	data = models.DateTimeField('Data a ser realizada:')
	descricao = models.TextField('Descrição da atividade:')
	
	def __str__(self):
		return self.nome

class Contato(models.Model):
	nome = models.CharField('Nome do usuáro:', max_length = 50)
	data = models.DateTimeField('Data de envio:')
	telefone = models.CharField('Nome do usuáro:', max_length = 50)
	email = models.CharField('Email do usuário:', max_length = 50)
	mensagem = models.TextField('Mensagem:')
	info = models.TextField('Informações do remetente:')

class Voluntario(models.Model):
	avatar = models.ImageField("Imagem do perfil", upload_to="imagens/voluntarios", blank = True, null = True)
	usuario = models.OneToOneField(User, related_name = "profile")

	def __str__(self):
		return self.usuario.username

	def avatar_image(self):
		return (MEDIA_URL + self.avatar.name) if self.avatar else None