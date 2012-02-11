#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from inventario.models import Inventario
from fonte_emissao.models import FonteEmissao


class FonteEmissaoECV(models.Model):
	TIPO_CHOICES=(
        (1, 'biomassa'),
        (2, 'fossil'),
    )
	tipo=models.IntegerField(verbose_name=u'Tipo de fonte',choices=TIPO_CHOICES)	
	combustivel=models.CharField(max_length=50)
	unidade=models.CharField(max_length=20,)
	caloria=models.FloatField(verbose_name=u'Poder Calorífico Inferior (GJ/t)')
	densidade=models.FloatField(verbose_name=u'Densidade (Kg/unidade)')		
	fatorco2=models.FloatField(verbose_name=u'Fator de CO2')
	fatorch4=models.FloatField(verbose_name=u'Fator de CH4 para o Setor de Energia')
	fatorn2o=models.FloatField(verbose_name=u'Fator de N2O para o Setor de Energia')
	
	def __unicode__(self):
		return unicode(self.combustivel)
	

class ECV(models.Model):
	inventario=models.OneToOneField(Inventario)
	fonte_emissao = models.ManyToManyField(FonteEmissaoECV, through='FonteECV', verbose_name= u'Lista de Emissões')
	
	def __unicode__(self):
		return unicode(self.inventario)
	
class FonteECV(models.Model):
	
	ecv=models.ForeignKey(ECV)
	fonte_emissao = models.ForeignKey(FonteEmissaoECV,verbose_name=u'Fonte de emissao')
	registro=models.CharField(max_length=50,verbose_name=u'Registro da fonte')
	descricao=models.CharField(max_length=75,verbose_name=u'Descrição da fonte')
	fervedor=models.FloatField(verbose_name=u'Eff Fervedor (%)')
	vapor=models.FloatField(verbose_name=u'Vapor Comprado (GJ)')
	
	def __unicode__(self):
		return unicode(self.fonte_emissao)

class TotalECV(models.Model):
	ecv=models.ForeignKey(ECV)
	ecv_fossil_co2=models.FloatField()
	ecv_fossil_ch4=models.FloatField()
	ecv_fossil_n2o=models.FloatField()
	ecv_bio_co2=models.FloatField()
	ecv_bio_ch4=models.FloatField()
	ecv_bio_n2o=models.FloatField()
	ecv_emissoes_equivalentes=models.FloatField()
	ecv_emissoes_biomassa=models.FloatField()
	
	def __unicode__(self):
		return unicode(self.ecv)
	
	
	

