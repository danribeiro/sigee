# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TotalRAC'
        db.create_table('emissao_rac_totalrac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rac', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emissao_rac.RAC'])),
            ('totalrac_co2', self.gf('django.db.models.fields.FloatField')()),
            ('emissoes_equivalentes_rac', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('emissao_rac', ['TotalRAC'])


    def backwards(self, orm):
        
        # Deleting model 'TotalRAC'
        db.delete_table('emissao_rac_totalrac')


    models = {
        'emissao_rac.equipamento': {
            'Meta': {'object_name': 'Equipamento'},
            'coe_dispensado': ('django.db.models.fields.FloatField', [], {}),
            'coe_novas': ('django.db.models.fields.FloatField', [], {}),
            'coe_operacional': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'emissao_rac.fonterac': {
            'Meta': {'object_name': 'FonteRAC'},
            'dispensado': ('django.db.models.fields.FloatField', [], {}),
            'equipamento_rac': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emissao_rac.Equipamento']"}),
            'gas_rac': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emissao_rac.Gas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'novas': ('django.db.models.fields.FloatField', [], {}),
            'operacional': ('django.db.models.fields.FloatField', [], {}),
            'rac': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emissao_rac.RAC']"}),
            'registro': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'emissao_rac.gas': {
            'Meta': {'object_name': 'Gas'},
            'gas': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gwp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'emissao_rac.rac': {
            'Meta': {'object_name': 'RAC'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventario.Inventario']", 'unique': 'True'})
        },
        'emissao_rac.totalrac': {
            'Meta': {'object_name': 'TotalRAC'},
            'emissoes_equivalentes_rac': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rac': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emissao_rac.RAC']"}),
            'totalrac_co2': ('django.db.models.fields.FloatField', [], {})
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

    complete_apps = ['emissao_rac']
