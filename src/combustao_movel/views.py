#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from inventario.models import Empresa, CED, Inventario, FonteCED

from forms import FormFonteECM, FormECM, FormFatores, FormParametros, FormFonteEmissaoECM
from models import FonteECM, ECM, FatoresVariaveis, Parametros, FonteEmissaoECM, TotalECM

from django.forms.models import  inlineformset_factory

#vies que manipulam os objetos da tabela ECM
def adiciona_ecm(request):
	if request.method=='POST':
		form=FormECM(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('ecm/add_ecm.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormECM()				
	return render_to_response('ecm/add_ecm.html',{'form':form},context_instance=RequestContext(request))

def remove_ecm(request,nr_item):
	item=ECM.objects.get(pk=nr_item)
	item.delete()
	return render_to_response('ecm/lista_ecm.html',context_instance=RequestContext(request))	
	
def lista_ecm(request):
	lista_itens=ECM.objects.all()
	return render_to_response('ecm/lista_ecm.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))

def edita_ecm(request,nr_item):
	objeto=ECM.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormECM(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('ecm/edita_ecm.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormECM(instance=objeto)
	return render_to_response('ecm/edita_ecm.html',{'form':form},context_instance=RequestContext(request))

###################################################################################
#views que manipulam os objetos da tabela FonteECM
def adiciona_fonteecm(request):
	if request.method=='POST':
		form=FormFonteECM(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fonteecm/add_fonteecm.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteECM()				
	return render_to_response('fonteecm/add_fonteecm.html',{'form':form},context_instance=RequestContext(request))
	
def lista_fonteecm(request):
	lista_itens=FonteECM.objects.all()
	context=RequestContext(request)
	return render_to_response('fonteecm/lista_fonteecm.html',{'lista_itens':lista_itens},context)
	
def remove_fonteecm(request,nr_item):
	item=get_object_or_404(FonteECM, pk=nr_item)
	item.delete()
	return render_to_response('fonteecm/lista_fonteecm.html',context_instance=RequestContext(request))

def edita_fonteecm(request,nr_item):
	objeto=FonteECM.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteECM(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonteecm/edita_fonteecm.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteECM(instance=objeto)
	return render_to_response('fonteecm/edita_fonteecm.html',{'form':form},context_instance=RequestContext(request))
	

###################################################################################


def adiciona_fator(request):
	#FatorFormSet=inlineformset_factory(FatoresVariaveis,Parametros)
	if request.method=='POST':
		form=FormFatores(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fatores/add_fator.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFatores()				
	return render_to_response('fatores/add_fator.html',{'form':form},context_instance=RequestContext(request))

def lista_fator(request):
	lista_itens=FatoresVariaveis.objects.all()
	context=RequestContext(request)
	return render_to_response('fatores/lista_fator.html',{'lista_itens':lista_itens},context)
	
def remove_fator(request,nr_item):
	item=get_object_or_404(FatoresVariaveis, pk=nr_item)
	item.delete()
	return render_to_response('fatores/lista_fator.html',context_instance=RequestContext(request))

def edita_fator(request,nr_item):
	objeto=FatoresVariaveis.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFatores(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fatores/edita_fator.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFatores(instance=objeto)
	return render_to_response('fatores/edita_fator.html',{'form':form},context_instance=RequestContext(request))
	


######
def adiciona_param(request):
	if request.method=='POST':
		form=FormParametros(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fatores/add_parametros.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormParametros()				
	return render_to_response('fatores/add_parametros.html',{'form':form},context_instance=RequestContext(request))

def lista_param(request):
	lista_itens=Parametros.objects.all()
	context=RequestContext(request)
	return render_to_response('fatores/lista_parametros.html',{'lista_itens':lista_itens},context)
	
def remove_param(request,nr_item):
	item=get_object_or_404(Parametros, pk=nr_item)
	item.delete()
	return render_to_response('fatores/lista_parametros.html',context_instance=RequestContext(request))
	
def edita_param(request,nr_item):
	objeto=Parametros.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormParametros(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fatores/edita_parametros.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormParametros(instance=objeto)
	return render_to_response('fatores/edita_parametros.html',{'form':form},context_instance=RequestContext(request))
	
################
def adiciona_emissaoecm(request):
	if request.method=='POST':
		form=FormFonteEmissaoECM(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fatores/add_emissaoecm.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteEmissaoECM()				
	return render_to_response('fatores/add_emissaoecm.html',{'form':form},context_instance=RequestContext(request))

def lista_emissaoecm(request):
	lista_itens=FonteEmissaoECM.objects.all()
	context=RequestContext(request)
	return render_to_response('fatores/lista_emissaoecm.html',{'lista_itens':lista_itens},context)
	
def remove_emissaoecm(request,nr_item):
	item=get_object_or_404(FonteEmissaoECM, pk=nr_item)
	item.delete()
	return render_to_response('fatores/lista_emissaoecm.html',context_instance=RequestContext(request))

def edita_emissaoecm(request,nr_item):
	objeto=FonteEmissaoECM.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteEmissaoECM(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fatores/edita_emissaoecm.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteEmissaoECM(instance=objeto)
	return render_to_response('fatores/edita_emissaoecm.html',{'form':form},context_instance=RequestContext(request))
	

######

def calcula_ecm(request, nr_item):
	ecm=get_object_or_404(ECM, pk=nr_item)     
	inventario_ano=Inventario.objects.get(pk=ecm.inventario_id)	
	emissoes=FonteECM.objects.all()
		
	fatores=FatoresVariaveis.objects.get(ano_param=inventario_ano.ano)
	parametros=Parametros.objects.all().filter(fatores_variaveis=fatores.id)
	
	bioco2=fossilco2=diesel=biodiesel=gasolina=etanol=fatoretanol=fatorbiodiesel=quantidade=0
	for item in emissoes:
		emissao=FonteECM.objects.get(pk=item.id)
		fonte=FonteEmissaoECM.objects.get(pk=emissao.fonte_emissao_id)
		#fator=FatoresVariaveis.objects.get(mes=emissao.mes)
		for parametro in parametros:
			if parametro.mes==item.mes:
				fatoretanol=parametro.etanol_gasolina/100
				fatorbiodiesel=parametro.biodiesel_diesel/100
		
		if fonte.tipo==1:#biomassa
			bioco2=bioco2+(fonte.fatorco2*emissao.quantidade)
				
		elif fonte.tipo==2:
			if fonte.combustivel==u'Óleo Diesel':#fóssil		
			
				diesel=1-fatorbiodiesel		
				fossilco2=fossilco2+(fonte.fatorco2*(emissao.quantidade*diesel))			
			
				fontebiodiesel=FonteEmissaoECM.objects.get(combustivel='Biodiesel(B100)') 			
					
				biodiesel=(fontebiodiesel.fatorco2*emissao.quantidade)*fatorbiodiesel
				bioco2=bioco2+biodiesel
				
			if fonte.combustivel==u'Gasolina':			
				gasolina=1-fatoretanol		
				fossilco2=fossilco2+(fonte.fatorco2*(emissao.quantidade*gasolina))
			
				fonteetanol=FonteEmissaoECM.objects.get(combustivel='Etanol(E100)')
				etanol=(fonteetanol.fatorco2*emissao.quantidade)*fatoretanol
				bioco2=bioco2+etanol
		else:	
			fossilco2=fossilco2+(fonte.fatorco2*emissao.quantidade)
		
		
	emissoes_equivalentes=fossilco2/1000
	emissoes_biomassa=bioco2/1000
	
	bioco2=round(bioco2,1)
	fossilco2=round(fossilco2,1)
	
	
	emissoes_equivalentes=round(emissoes_equivalentes,1)
	emissoes_biomassa=round(emissoes_biomassa,1)
	
	###########################################################
	#salvo os totais da tabela de TotalECM
	total=TotalECM(
	ecm=ecm,
	ecm_fossil_co2=fossilco2,
	ecm_bio_co2=bioco2,
	ecm_emissoes_equivalentes=emissoes_equivalentes,
	ecm_emissoes_biomassa=emissoes_biomassa,
	)
	total.save()
	##########################################################
	
	return render_to_response('ecm/resumo_ecm.html',{'emissoes_equivalentes':emissoes_equivalentes,
													 'emissoes_biomassa':emissoes_biomassa,
													 'fossilco2':fossilco2,
													 'bioco2':bioco2,
													 'etanol':etanol,
													 'quantidade':quantidade,
													 'gasolina':gasolina},													
													 context_instance=RequestContext(request))
		
			
			
			 
				
				
				
		
		
	

	
