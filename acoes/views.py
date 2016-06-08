from django.shortcuts import render, get_object_or_404
from acoes.models import Entidade, Acao, Campanha, Calendario, Voluntario
from acoes.forms import CadastroVoluntario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from django.conf import settings
# Create your views here.
# Informações sobre as views.


# INDEX
def index(reques):
	return render(request, 'index.html')

# ENTIDADES
def entities(request, pagina=1):
	paginacao = Paginator(Entidade.objects.all(), 5)

	try:
		resumo = paginacao.page(pagina)
	except PageNotAnInteger:
		# Se a página não for um inteiro, pega a primeira
		resumo = paginacao.page(1)
	except EmptyPage:
		# Se a página estiver fora do limite, pega a última
		resumo = paginacao.page(paginacao.num_pages)

	return render(request, 'entities.html', {
		'entidades': resumo.object_list,
		'media_url': settings.MEDIA_URL,
		'paginacao': resumo,
		'page_now': pagina,
		})

def entity(request, url):
	return render(request, 'entity.html', {
		'entidade': get_object_or_404(Entidade, url=url), #Pegando em artigo o objeto com a url informada
		'media_url': settings.MEDIA_URL,
		})

# CAMPANHAS
def campaigns(request, pagina = 1):

	paginacao = Paginator(Campanha.objects.all().order_by('-id'), 6)

	try:
		resumo = paginacao.page(pagina)
	except PageNotAnInteger:
		resumo = paginacao.page(1)
	except EmptyPage:
		resumo = paginacao.page(paginacao.num_pages)

	return render(request, 'campaigns.html', {
		'campanhas': resumo.object_list,
		'media_url': settings.MEDIA_URL,
		'paginacao': resumo,
		'page_now': pagina,
		})
def campaign(request, url):
	return render(request, 'campaign.html', {
		'campanha' : get_object_or_404(Campanha, url=url),
		'media_url': settings.MEDIA_URL,
		})

# ACOES
def actions(request, pagina = 1):

	paginacao = Paginator(Acao.objects.all().order_by('-id'), 9)

	try:
		resumo = paginacao.page(pagina)
	except PageNotAnInteger:
		resumo = paginacao.page(1)
	except EmptyPage:
		resumo = paginacao.page(paginacao.num_pages)

	return render(request, 'actions.html', {
		'acoes': resumo.object_list,
		'media_url': settings.MEDIA_URL,
		'paginacao': resumo,
		'page_now': pagina,
		})

def action(request, url):
	return render(request, 'action.html', {
		'acao': get_object_or_404(Acao, url=url),
		'media_url': settings.MEDIA_URL,
		})

# FORMULÁRIO DE PESQUISA
def search_form(request):

	return HttpResponse("Welcome to the page at %s" % request.META)
    # if 'q' in request.GET and request.GET['q']:
    #     q = request.GET['q']

       
       	# return render(request, 'index.html')
        # if request.path == '/entidades/':
    # else:
    	# return render(request, 'action.html')

    #     artigos = Artigo.objects.filter(titulo__contains=q) | Artigo.objects.filter(conteudo__contains=q)
    #     artigos = Artigo.objects.filter(titulo__contains=q) | Artigo.objects.filter(conteudo__contains=q)
    #     artigos = Artigo.objects.filter(titulo__contains=q) | Artigo.objects.filter(conteudo__contains=q)
    #     return render(request, 'search_results.html',
    #         {'artigos': artigos, 'query': q})
    # else:
    #     return HttpResponse('Por favor, informe um termo para a pesquisa!')

def contact(request):

	stat = False

	if request.GET['enviar']:
		name        = request.GET['nome']
		tel         = request.GET['telefone']
		email       = request.GET['email']
		mensagem    = request.GET['mensagem']
		info        = request.META

		stat = True

		from acoes.models import Contato
		contato = Contato(nome = name, data = datetime.datetime.now(), telefone = tel, email = email, mensagem = mensagem, info = info)
		contato.save()

	return render(request, 'contact.html', stat)

def calendar(request, pagina = 1):

	paginacao = Paginator(Calendario.objects.all().order_by('-id'), 5)

	try:
		resumo = paginacao.page(pagina)
	except PageNotAnInteger:
		resumo = paginacao.page(1)
	except EmptyPage:
		resumo = paginacao.page(paginacao.num_pages)

	return render(request, 'calendar.html', {
		'calendario': resumo.object_list,
		'media_url': settings.MEDIA_URL,
		'paginacao': resumo,
		'page_now': pagina,
		})

def registroVoluntario(request):
    if request.method == "POST":
        form = CadastroVoluntario(request.POST, request.FILES)
        if form.is_valid():
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(user, email, password)

            new_profile = Voluntario(avatar = request.FILES['avatar'], user=new_user)
            new_profile.save()
            user_authenticated = authenticate(username=user, password=password)
            login(request, user_authenticated)

            return HttpResponseRedirect('/')
    else:
        form = CadastroVoluntario()

    return render(request, 'register.html',{
        "form":form
    })