# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TotalECM'
        db.create_table('combustao_movel_totalecm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ecm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['combustao_movel.ECM'])),
            ('ecm_fossil_co2', self.gf('django.db.models.fields.FloatField')()),
            ('ecm_bio_co2', self.gf('django.db.models.fields.FloatField')()),
            ('ecm_emissoes_equivalentes', self.gf('django.db.models.fields.FloatField')()),
            ('ecm_emissoes_biomassa', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('combustao_movel', ['TotalECM'])


    def backwards(self, orm):
        
        # Deleting model 'TotalECM'
        db.delete_table('combustao_movel_totalecm')


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
        'combustao_movel.totalecm': {
            'Meta': {'object_name': 'TotalECM'},
            'ecm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['combustao_movel.ECM']"}),
            'ecm_bio_co2': ('django.db.models.fields.FloatField', [], {}),
            'ecm_emissoes_biomassa': ('django.db.models.fields.FloatField', [], {}),
            'ecm_emissoes_equivalentes': ('django.db.models.fields.FloatField', [], {}),
            'ecm_fossil_co2': ('django.db.models.fields.FloatField', [], {}),
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

    complete_apps = ['combustao_movel']
