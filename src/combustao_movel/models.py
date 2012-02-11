#-*- coding: utf-8 -*-
from django.db import models
from inventario.models import Inventario

MONTH_CHOICES=(
	(1,'Janeiro'),
	(2,'Fevereiro'),
	(3,'Março'),
	(4,'Abril'),
	(5,'Maio'),
	(6,'Junho'),
	(7,'Julho'),
	(8,'Agosto'),
	(9,'Setembro'),
	(10,'Outubro'),
	(11,'Novembro'),
	(12,'Dezembro'),
	)

class FonteEmissaoECM(models.Model):
	TIPO_CHOICES=(
	(1,'biomassa'),
	(2,'fossil'),
	)
	combustivel=models.CharField(max_length=50,verbose_name=u'Combustível')
	tipo=models.IntegerField(choices=TIPO_CHOICES)
	unidade=models.CharField(max_length=50)
	fatorco2=models.FloatField(verbose_name=u'Fator de Emissão de CO2')
	
	def __unicode__(self):
		return unicode(self.combustivel)
	

class ECM(models.Model):
	inventario=models.OneToOneField(Inventario, verbose_name=u'Inventário')
	fontes_emissao=models.ManyToManyField(FonteEmissaoECM, through='FonteECM', verbose_name= u'Lista de Emissões')
	
	def __unicode__(self):
		return unicode(self.inventario)  

class FonteECM(models.Model):
	
	ecm = models.ForeignKey(ECM, verbose_name=u'ECM Relacionado')
	fonte_emissao = models.ForeignKey(FonteEmissaoECM, verbose_name=u'Fonte de emissão')
	quantidade = models.FloatField(verbose_name=u'Valor relativo ao mês')
	registro_fonte = models.CharField(max_length=50)
	descricao_fonte = models.CharField(max_length = 75)	
	mes=models.IntegerField(choices=MONTH_CHOICES,verbose_name=u'Mês')
	
	def __unicode__(self):
		return unicode(self.fonte_emissao)	
    	

class FatoresVariaveis(models.Model):
	YEAR_CHOICES=(
	(1,'2009'),
	(2,'2010'),
	(3,'2011'),
	)
	ano_param=models.IntegerField(choices=YEAR_CHOICES,verbose_name=u'Ano Relativo ')	
	
	def __unicode__(self):
		return unicode(self.ano_param)
	
	
class Parametros(models.Model):
	fatores_variaveis=models.ForeignKey(FatoresVariaveis,verbose_name=u'Fatores Variaveis')
	etanol_gasolina=models.FloatField(verbose_name=u'Porcentagem de Etanol(E100) na Gasolina')
	biodiesel_diesel=models.FloatField(verbose_name=u'Porcentagem de Biodiesel(B100) no Diesel')
	fesin=models.FloatField(verbose_name=u'Fator de Emissão de Energia Elétrica do SIN')
	mes=models.IntegerField(choices=MONTH_CHOICES,verbose_name=u'Mês')
	
	def __unicode__(self):
		return unicode(self.fatores_variaveis)
		

class TotalECM(models.Model):
	ecm=models.ForeignKey(ECM)
	ecm_fossil_co2=models.FloatField()
	ecm_bio_co2=models.FloatField()
	ecm_emissoes_equivalentes=models.FloatField()
	ecm_emissoes_biomassa=models.FloatField()
	
	def __unicode__(self):
		return unicode(self.ecm)

		
	
	
	
