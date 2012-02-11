# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'TotalCED', fields ['ced']
        db.delete_unique('inventario_totalced', ['ced_id'])

        # Changing field 'TotalCED.ced'
        db.alter_column('inventario_totalced', 'ced_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.CED']))


    def backwards(self, orm):
        
        # Changing field 'TotalCED.ced'
        db.alter_column('inventario_totalced', 'ced_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventario.CED'], unique=True))

        # Adding unique constraint on 'TotalCED', fields ['ced']
        db.create_unique('inventario_totalced', ['ced_id'])


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
        },
        'inventario.totalced': {
            'Meta': {'object_name': 'TotalCED'},
            'bioced_ch4': ('django.db.models.fields.FloatField', [], {}),
            'bioced_co2': ('django.db.models.fields.FloatField', [], {}),
            'bioced_n2o': ('django.db.models.fields.FloatField', [], {}),
            'ced': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventario.CED']"}),
            'emissoes_biomassa_ced': ('django.db.models.fields.FloatField', [], {}),
            'emissoes_equivalentes_ced': ('django.db.models.fields.FloatField', [], {}),
            'fossilced_ch4': ('django.db.models.fields.FloatField', [], {}),
            'fossilced_co2': ('django.db.models.fields.FloatField', [], {}),
            'fossilced_n2o': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inventario']
