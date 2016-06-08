from django.conf.urls import patterns, include, url
from django.conf import settings
# from VoluntariosBem.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # HOME
    url(r'^$', 'VoluntariosBem.views.index'),

    # RESULTADO DE PESQUISA
    # url(r'^resultado-pesquisa/$', 'acoes.views.search_form'),

    # SOBRE
    url(r'^sobre/$', 'VoluntariosBem.views.about'),

    # CONTATO
    url(r'^contato/$', 'VoluntariosBem.views.contact'),
    url(r'^enviar-mensagem/$', 'acoes.views.contact'),

    #Parceiros e patrocinadores
    url(r'^parceiros/$', 'VoluntariosBem.views.partners'),

    # Ações
    url(r'^acoes/$', 'acoes.views.actions'),
    url(r'^acoes/pagina/(?P<pagina>[^\.]+)', 'acoes.views.actions'),
    url(r'^acoes/(?P<url>[^\.]+)$','acoes.views.action'),

    # Entidades
    url(r'^entidades/$', 'acoes.views.entities', {'pagina': 1}),
    url(r'^entidades/pagina/(?P<pagina>[^\.]+)', 'acoes.views.entities'),
    url(r'^entidades/(?P<url>[^\.]+)$','acoes.views.entity'),

    # Campanhas
    url(r'^campanhas/$', 'acoes.views.campaigns'),
    url(r'^campanhas/pagina/(?P<pagina>[^\.]+)', 'acoes.views.campaigns'),
    url(r'^campanhas/(?P<url>[^\.]+)$','acoes.views.campaign'),

    # Calendário
    url(r'^calendario/$', 'acoes.views.calendar'),
    url(r'^calendario/pagina/(?P<pagina>[^\.]+)', 'acoes.views.calendar'),

    #Perfil Voluntário
    url(r'^profile/(?P<mfpk>\d+)/$', 'acoes.views.index', {}, "profile"),

    # Cadastro de voluntário
    url(r'^cadastro-voluntario/', 'acoes.views.registroVoluntario'),

    # Área administrativa
    url(r'^admin/', include(admin.site.urls)),

    # Arquivos estáticos: CSS, JS...
    # url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)

if settings.LOCAL:
    urlpatterns += patterns('',
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )