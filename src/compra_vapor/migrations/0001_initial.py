# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FonteEmissaoECV'
        db.create_table('compra_vapor_fonteemissaoecv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('combustivel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('unidade', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('caloria', self.gf('django.db.models.fields.FloatField')()),
            ('densidade', self.gf('django.db.models.fields.FloatField')()),
            ('fatorco2', self.gf('django.db.models.fields.FloatField')()),
            ('fatorch4', self.gf('django.db.models.fields.FloatField')()),
            ('fatorn2o', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('compra_vapor', ['FonteEmissaoECV'])

        # Adding model 'ECV'
        db.create_table('compra_vapor_ecv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inventario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventario.Inventario'], unique=True)),
        ))
        db.send_create_signal('compra_vapor', ['ECV'])

        # Adding model 'FonteECV'
        db.create_table('compra_vapor_fonteecv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ecv', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compra_vapor.ECV'])),
            ('fonte_emissao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compra_vapor.FonteEmissaoECV'])),
            ('registro', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('fervedor', self.gf('django.db.models.fields.FloatField')()),
            ('vapor', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('compra_vapor', ['FonteECV'])


    def backwards(self, orm):
        
        # Deleting model 'FonteEmissaoECV'
        db.delete_table('compra_vapor_fonteemissaoecv')

        # Deleting model 'ECV'
        db.delete_table('compra_vapor_ecv')

        # Deleting model 'FonteECV'
        db.delete_table('compra_vapor_fonteecv')


    models = {
        'compra_vapor.ecv': {
            'Meta': {'object_name': 'ECV'},
            'fonte_emissao': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compra_vapor.FonteEmissaoECV']", 'through': "orm['compra_vapor.FonteECV']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventario.Inventario']", 'unique': 'True'})
        },
        'compra_vapor.fonteecv': {
            'Meta': {'object_name': 'FonteECV'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'ecv': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compra_vapor.ECV']"}),
            'fervedor': ('django.db.models.fields.FloatField', [], {}),
            'fonte_emissao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compra_vapor.FonteEmissaoECV']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vapor': ('django.db.models.fields.FloatField', [], {})
        },
        'compra_vapor.fonteemissaoecv': {
            'Meta': {'object_name': 'FonteEmissaoECV'},
            'caloria': ('django.db.models.fields.FloatField', [], {}),
            'combustivel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'densidade': ('django.db.models.fields.FloatField', [], {}),
            'fatorch4': ('django.db.models.fields.FloatField', [], {}),
            'fatorco2': ('django.db.models.fields.FloatField', [], {}),
            'fatorn2o': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'unidade': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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

    complete_apps = ['compra_vapor']
