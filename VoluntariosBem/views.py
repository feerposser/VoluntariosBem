from django.http import HttpResponse , Http404
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render

# HOME
def index(request):
    # return HttpResponse("Olá mundo!")
    # t = get_template('index.html')
    # html = t.render(Context({'variavel': valor}))

    # return HttpResponse(t)
    # return render(request, 'index.html', {'variavel':valor})
    return render(request, 'index.html')

# SOBRE
def about(request):
	return render(request, 'about.html')

# CONTATO
def contact(request):
    return render(request, 'contact.html')

# PARCEIROS E PATROCINADORES
def partners(request):
	return render(request, 'partners.html')

# ENTIDADES
def entities(request):
	return render(request, 'entities.html')

def entity(request):
    return render(request, 'entity.html')

# AÇÕES
def actions(request):
	return render(request, 'actions.html')

# CAMPANHAS
def campaigns(request):
    return render(request, 'campaigns.html')

def campaign(request):
    return render(request, 'campaign.html')