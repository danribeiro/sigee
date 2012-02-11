# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ECE'
        db.create_table('compra_energia_ece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inventario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventario.Inventario'], unique=True)),
        ))
        db.send_create_signal('compra_energia', ['ECE'])

        # Adding model 'FonteECE'
        db.create_table('compra_energia_fonteece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compra_energia.ECE'])),
            ('quantidade', self.gf('django.db.models.fields.FloatField')()),
            ('registro_fonte', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao_fonte', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('mes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('compra_energia', ['FonteECE'])


    def backwards(self, orm):
        
        # Deleting model 'ECE'
        db.delete_table('compra_energia_ece')

        # Deleting model 'FonteECE'
        db.delete_table('compra_energia_fonteece')


    models = {
        'compra_energia.ece': {
            'Meta': {'object_name': 'ECE'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventario.Inventario']", 'unique': 'True'})
        },
        'compra_energia.fonteece': {
            'Meta': {'object_name': 'FonteECE'},
            'descricao_fonte': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'ece': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compra_energia.ECE']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {}),
            'quantidade': ('django.db.models.fields.FloatField', [], {}),
            'registro_fonte': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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

    complete_apps = ['compra_energia']
