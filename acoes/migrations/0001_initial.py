# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entidade'
        db.create_table('acoes_entidade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('conteudo', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('acoes', ['Entidade'])

        # Adding model 'Acao'
        db.create_table('acoes_acao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('situacao', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('acoes', ['Acao'])

        # Adding M2M table for field entidade on 'Acao'
        m2m_table_name = db.shorten_name('acoes_acao_entidade')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acao', models.ForeignKey(orm['acoes.acao'], null=False)),
            ('entidade', models.ForeignKey(orm['acoes.entidade'], null=False))
        ))
        db.create_unique(m2m_table_name, ['acao_id', 'entidade_id'])

        # Adding model 'Campanha'
        db.create_table('acoes_campanha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('acoes', ['Campanha'])


    def backwards(self, orm):
        # Deleting model 'Entidade'
        db.delete_table('acoes_entidade')

        # Deleting model 'Acao'
        db.delete_table('acoes_acao')

        # Removing M2M table for field entidade on 'Acao'
        db.delete_table(db.shorten_name('acoes_acao_entidade'))

        # Deleting model 'Campanha'
        db.delete_table('acoes_campanha')


    models = {
        'acoes.acao': {
            'Meta': {'object_name': 'Acao'},
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'entidade': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['acoes.Entidade']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'situacao': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'acoes.campanha': {
            'Meta': {'object_name': 'Campanha'},
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'acoes.entidade': {
            'Meta': {'object_name': 'Entidade'},
            'conteudo': ('django.db.models.fields.TextField', [], {}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['acoes']