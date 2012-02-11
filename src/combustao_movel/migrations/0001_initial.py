# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FonteEmissaoECM'
        db.create_table('combustao_movel_fonteemissaoecm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('combustivel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('unidade', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fatorco2', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('combustao_movel', ['FonteEmissaoECM'])

        # Adding model 'ECM'
        db.create_table('combustao_movel_ecm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inventario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventario.Inventario'], unique=True)),
        ))
        db.send_create_signal('combustao_movel', ['ECM'])

        # Adding model 'FonteECM'
        db.create_table('combustao_movel_fonteecm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ecm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['combustao_movel.ECM'])),
            ('fonte_emissao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['combustao_movel.FonteEmissaoECM'])),
            ('quantidade', self.gf('django.db.models.fields.FloatField')()),
            ('registro_fonte', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao_fonte', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('mes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('combustao_movel', ['FonteECM'])

        # Adding model 'FatoresVariaveis'
        db.create_table('combustao_movel_fatoresvariaveis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ano_param', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('combustao_movel', ['FatoresVariaveis'])

        # Adding model 'Parametros'
        db.create_table('combustao_movel_parametros', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fatores_variaveis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['combustao_movel.FatoresVariaveis'])),
            ('etanol_gasolina', self.gf('django.db.models.fields.FloatField')()),
            ('biodiesel_diesel', self.gf('django.db.models.fields.FloatField')()),
            ('fesin', self.gf('django.db.models.fields.FloatField')()),
            ('mes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('combustao_movel', ['Parametros'])


    def backwards(self, orm):
        
        # Deleting model 'FonteEmissaoECM'
        db.delete_table('combustao_movel_fonteemissaoecm')

        # Deleting model 'ECM'
        db.delete_table('combustao_movel_ecm')

        # Deleting model 'FonteECM'
        db.delete_table('combustao_movel_fonteecm')

        # Deleting model 'FatoresVariaveis'
        db.delete_table('combustao_movel_fatoresvariaveis')

        # Deleting model 'Parametros'
        db.delete_table('combustao_movel_parametros')


    models = {
        'combustao_movel.ecm': {
            'Meta': {'object_name': 'ECM'},
            'fontes_emissao': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['combustao_movel.FonteEmissaoECM']", 'through': "orm['combustao_movel.FonteECM']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventario.Inventario']", 'unique': 'True'})
        },
        'combustao_movel.fatoresvariaveis': {
            'Meta': {'object_name': 'FatoresVariaveis'},
            'ano_param': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'combustao_movel.fonteecm': {
            'Meta': {'object_name': 'FonteECM'},
            'descricao_fonte': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'ecm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['combustao_movel.ECM']"}),
            'fonte_emissao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['combustao_movel.FonteEmissaoECM']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {}),
            'quantidade': ('django.db.models.fields.FloatField', [], {}),
            'registro_fonte': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'combustao_movel.fonteemissaoecm': {
            'Meta': {'object_name': 'FonteEmissaoECM'},
            'combustivel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fatorco2': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'unidade': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'combustao_movel.parametros': {
            'Meta': {'object_name': 'Parametros'},
            'biodiesel_diesel': ('django.db.models.fields.FloatField', [], {}),
            'etanol_gasolina': ('django.db.models.fields.FloatField', [], {}),
            'fatores_variaveis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['combustao_movel.FatoresVariaveis']"}),
            'fesin': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {})
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
        'inventario.inventario': {
            'Meta': {'object_name': 'Inventario'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventario.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['combustao_movel']
