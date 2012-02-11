#-*- coding: utf-8 -*- 

from django.db import models
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from fonte_emissao.models import SetorAtividade, FonteEmissao

# Create your models here.
class Empresa(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length = 10)
    bairro = models.CharField(max_length = 50)
    cep = models.CharField(max_length = 9)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices = STATE_CHOICES)
    
    def __unicode__(self):
    	return unicode(self.nome)    
    
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, verbose_name=u'Empresa Relacionada')
    data = models.DateField(auto_now_add=True)
    ano=models.IntegerField()
    
    def __unicode__(self):
    	return unicode(self.empresa)    
        
class CED(models.Model):
    inventario = models.OneToOneField(Inventario, verbose_name=u'Inventario')
    setor_atividade = models.ForeignKey(SetorAtividade,verbose_name=u'Setor de Atividade')
    fontes_emissao = models.ManyToManyField(FonteEmissao, through='FonteCED', verbose_name= u'Lista de Emissões')
    
    def __unicode__(self):
    	return unicode(self.inventario)    
    
class FonteCED(models.Model):
    ced = models.ForeignKey(CED, verbose_name=u'CED Relacionado')
    fonte_emissao = models.ForeignKey(FonteEmissao, verbose_name=u'Fonte de emissao')
    quantidade = models.FloatField()
    registro_fonte = models.CharField(max_length=50)
    descricao_fonte = models.CharField(max_length = 75)
    
    def __unicode__(self):
    	return unicode(self.fonte_emissao)

class TotalCED(models.Model):
	ced=models.ForeignKey(CED)
	data=models.DateField(auto_now_add=True)
	fossilced_co2=models.FloatField()
	fossilced_ch4=models.FloatField()
	fossilced_n2o=models.FloatField()
	bioced_co2=models.FloatField()
	bioced_ch4=models.FloatField()
	bioced_n2o=models.FloatField()
	emissoes_equivalentes_ced=models.FloatField()
	emissoes_biomassa_ced=models.FloatField()
	
	class Meta:
		get_latest_by='data'
	
	
		
    
   

