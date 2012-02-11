# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Empresa'
        db.create_table('inventario_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rua', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('inventario', ['Empresa'])

        # Adding model 'Inventario'
        db.create_table('inventario_inventario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Empresa'])),
            ('data', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('inventario', ['Inventario'])

        # Adding model 'CED'
        db.create_table('inventario_ced', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inventario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventario.Inventario'], unique=True)),
            ('setor_atividade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fonte_emissao.SetorAtividade'])),
        ))
        db.send_create_signal('inventario', ['CED'])

        # Adding model 'FonteCED'
        db.create_table('inventario_fonteced', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ced', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.CED'])),
            ('fonte_emissao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fonte_emissao.FonteEmissao'])),
            ('quantidade', self.gf('django.db.models.fields.FloatField')()),
            ('registro_fonte', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao_fonte', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('inventario', ['FonteCED'])


    def backwards(self, orm):
        
        # Deleting model 'Empresa'
        db.delete_table('inventario_empresa')

        # Deleting model 'Inventario'
        db.delete_table('inventario_inventario')

        # Deleting model 'CED'
        db.delete_table('inventario_ced')

        # Deleting model 'FonteCED'
        db.delete_table('inventario_fonteced')


    models = {
        'fonte_emissao.efsetor': {
            'Meta': {'object_name': 'EfSetor'},
            'ef_ch4': ('django.db.models.fields.FloatField', [], {}),
            'ef_n2o': ('django.db.models.fields.FloatField', [], {}),
            'fonte_emissao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fonte_emissao.FonteEmissao']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'setor_atividade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fonte_emissao.SetorAtividade']"})
        },
        'fonte_emissao.fonteemissao': {
            'Meta': {'object_name': 'FonteEmissao'},
            'ef_co2': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'unidade': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'fonte_emissao.setoratividade': {
            'Meta': {'object_name': 'SetorAtividade'},
            'fonte_emissao': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fonte_emissao.FonteEmissao']", 'through': "orm['fonte_emissao.EfSetor']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventario.ced': {
            'Meta': {'object_name': 'CED'},
            'fontes_emissao': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fonte_emissao.FonteEmissao']", 'through': "orm['inventario.FonteCED']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventario.Inventario']", 'unique': 'True'}),
            'setor_atividade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fonte_emissao.SetorAtividade']"})
        },
        'inventario.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventario.fonteced': {
            'Meta': {'object_name': 'FonteCED'},
            'ced': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventario.CED']"}),
            'descricao_fonte': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'fonte_emissao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fonte_emissao.FonteEmissao']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantidade': ('django.db.models.fields.FloatField', [], {}),
            'registro_fonte': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'inventario.inventario': {
            'Meta': {'object_name': 'Inventario'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventario.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inventario']
