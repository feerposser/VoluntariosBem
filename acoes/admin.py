from django.contrib import admin
from acoes.models import Entidade, Acao, Campanha, Calendario, Contato, Voluntario

# Register your models here.
# Informações que serão mostradas na área administrativa

class EntidadeAdmin(admin.ModelAdmin):
	list_display = ('nome', 'site')
	search_fields = ('nome', 'email')
	list_filter = ('nome',)
	ordering = ('nome',)
	fields = ('nome', 'url', 'imagemEntidade', 'site', 'conteudo', 'facebook', 'data')
	prepopulated_fields = {'url': ('nome',)}

class AcaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'data', 'situacao')
	search_fields = ('nome',)
	list_filter = ('nome',)
	ordering = ('nome',)
	# date_hierarchy = 'data_publicacao'
	fields = ('nome', 'url', 'imagemAcao', 'situacao', 'data', 'entidade', 'descricao')
	prepopulated_fields = {'url': ('nome',)}
	filter_horizontal = ('entidade',)

class CampanhaAdmin(admin.ModelAdmin):
	list_display = ('nome',)
	search_fields = ('nome',)
	list_filter = ('nome',)
	ordering = ('nome',)
	# date_hierarchy = 'data_publicacao'
	fields = ('nome', 'url', 'imagemCampanha', 'data', 'facebook', 'descricao')
	prepopulated_fields = {'url': ('nome',)}

class CalendarioAdmin(admin.ModelAdmin):
	list_display = ('nome',)
	search_fields = ('nome',)
	list_filter = ('nome',)
	ordering = ('nome',)
	fields = ('nome', 'url', 'imagemCalendario', 'data', 'descricao')
	date_hierarchy = 'data'
	prepopulated_fields = {'url': ('nome',)}

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'data')
	search_fields = ('nome', 'email', 'mensagem')
	list_filter = ('nome',)
	date_hierarchy = 'data'
	fields = ('nome', 'data', 'telefone', 'email', 'mensagem', 'info')

admin.site.register(Entidade, EntidadeAdmin)
admin.site.register(Acao, AcaoAdmin)
admin.site.register(Campanha, CampanhaAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Voluntario)