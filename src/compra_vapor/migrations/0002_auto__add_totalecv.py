# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TotalECV'
        db.create_table('compra_vapor_totalecv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ecv', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compra_vapor.ECV'])),
            ('ecv_fossil_co2', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_fossil_ch4', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_fossil_n2o', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_bio_co2', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_bio_ch4', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_bio_n2o', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_emissoes_equivalentes', self.gf('django.db.models.fields.FloatField')()),
            ('ecv_emissoes_biomassa', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('compra_vapor', ['TotalECV'])


    def backwards(self, orm):
        
        # Deleting model 'TotalECV'
        db.delete_table('compra_vapor_totalecv')


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
        'compra_vapor.totalecv': {
            'Meta': {'object_name': 'TotalECV'},
            'ecv': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compra_vapor.ECV']"}),
            'ecv_bio_ch4': ('django.db.models.fields.FloatField', [], {}),
            'ecv_bio_co2': ('django.db.models.fields.FloatField', [], {}),
            'ecv_bio_n2o': ('django.db.models.fields.FloatField', [], {}),
            'ecv_emissoes_biomassa': ('django.db.models.fields.FloatField', [], {}),
            'ecv_emissoes_equivalentes': ('django.db.models.fields.FloatField', [], {}),
            'ecv_fossil_ch4': ('django.db.models.fields.FloatField', [], {}),
            'ecv_fossil_co2': ('django.db.models.fields.FloatField', [], {}),
            'ecv_fossil_n2o': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
