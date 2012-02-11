# Create your views here.
#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import FormEmpresa, FormInventario, FormCED, FormFonteCED
from django.http import HttpResponse, HttpResponseRedirect
from inventario.models import Empresa, CED, Inventario, FonteCED, TotalCED
from fonte_emissao.models import SetorAtividade, FonteEmissao, EfSetor
from  django.utils.translation import  ugettext as _
from  django.core.exceptions import  ValidationError




#######################################################################################################################################
#views que gerenciam a tabela de empresas
def adiciona_empresa(request):
	if request.method=='POST':
		form=FormEmpresa(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('empresa/add_empresa.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormEmpresa()				
	return render_to_response('empresa/add_empresa.html',{'form':form},context_instance=RequestContext(request))

def remove_empresa(request,nr_item):
	item=get_object_or_404(Empresa, pk=nr_item)
	item.delete()
	return render_to_response('empresa/lista_empresa.html',context_instance=RequestContext(request))
	
def lista_empresa(request):
	lista_itens=Empresa.objects.all()
	context=RequestContext(request)
	return render_to_response('empresa/lista_empresa.html',{'lista_itens':lista_itens},context)
	
def edita_empresa(request,nr_item):
	objeto=Empresa.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormEmpresa(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('empresa/edita_empresa.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormEmpresa(instance=objeto)
	return render_to_response('empresa/edita_empresa.html',{'form':form},context_instance=RequestContext(request))

	
#######################################################################################################################################
#views que gerenciam a tabela de inventario
def inicia_inventario(request):	
	if request.method=='POST':
		form=FormInventario(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('inventario/adiciona_inventario.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormInventario()
	return render_to_response('inventario/adiciona_inventario.html',{'form':form}, context_instance=RequestContext(request))
		
def lista_inventario(request):
	lista_itens=Inventario.objects.all()
	context=RequestContext(request)
	return render_to_response('inventario/lista_inventario.html',{'lista_itens':lista_itens},context)
	
def remove_inventario(request,nr_item):
	item=get_object_or_404(Inventario, pk=nr_item)
	item.delete()
	return render_to_response('inventario/lista_inventario.html',context_instance=RequestContext(request))
	
def edita_inventario(request,nr_item):
	objeto=Inventario.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormInventario(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('inventario/edita_inventario.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormInventario(instance=objeto)
	return render_to_response('inventario/edita_inventario.html',{'form':form},context_instance=RequestContext(request))

	
#######################################################################################################################################		
#views que gerenciam a tabela de Emissão Por combustão Estacionária 
def adiciona_ced(request):
	if request.method=='POST':
		form=FormCED(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('ced/add_ced.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = FormCED()
	return render_to_response('ced/add_ced.html',{'form':form},context_instance=RequestContext(request))
	

def calcula_ced(request,nr_item):
	ced=get_object_or_404(CED, pk=nr_item)	
	setor=SetorAtividade.objects.get(pk=ced.setor_atividade_id)		
	emissoes=FonteCED.objects.all()
	
	bioch4=bion2o=fossilch4=fossiln2o=bioco2=fossilco2=emissoes_equivalentes=emissoes_biomassa=fatorch4=fatorn2o=0
	
	qs=EfSetor.objects.all()
	qs=EfSetor.objects.filter(setor_atividade=setor)
	
	for item in emissoes:
		emissao=FonteCED.objects.get(pk=item.id)	
		fonte=FonteEmissao.objects.get(pk=emissao.fonte_emissao_id)	
		
		for x in qs:
			if x.pk==fonte.pk:
				fatorch4=x.ef_ch4
				fatorn2o=x.ef_n2o				
		
		if fonte.tipo==1:#biomassa
			bioco2=bioco2+(fonte.ef_co2*emissao.quantidade)
			bioch4=bioch4+(emissao.quantidade*fatorch4)
			bion2o=bion2o+(emissao.quantidade*fatorn2o)	
	
		elif fonte.tipo==2:#fóssil	
			fossilco2=fossilco2+(fonte.ef_co2*emissao.quantidade)
			fossilch4=fossilch4+(emissao.quantidade*fatorch4)
			fossiln2o=fossiln2o+(emissao.quantidade*fatorn2o)
		
	totalch4=(bioch4+fossilch4)*21 # GWP CH4 = 21 
	totaln2o=(bion2o+fossiln2o)*310 # GWP N2O = 310 	
			
	emissoes_equivalentes=(fossilco2+totalch4+totaln2o)/1000 	#calcula o total de emissões equivalentes (toneladas métricas)		
	emissoes_biomassa=bioco2/1000					#calcula o total de emissões equivalentes de Biomassa (toneladas metricas)		
		
		
	#truncando os valores para renderização 
	emissoes_biomassa=round(emissoes_biomassa,1)		
	emissoes_equivalentes=round(emissoes_equivalentes,1)	 
	fossilco2=round(fossilco2,1)
	fossilch4=round(fossilch4,1)
	fossiln2o=round(fossiln2o,1)
	bioch4=round(bioch4,1)
	bion2o=round(bion2o,1)
	bioco2=round(bioco2,1)
	
	##############################################################
	#salvo os totais na tabela TotaCED
	total=TotalCED(
	ced=ced,
	fossilced_co2=fossilco2,
	fossilced_ch4=fossilch4,
	fossilced_n2o=fossiln2o,
	bioced_co2=bioco2,
	bioced_ch4=bioch4,
	bioced_n2o=bion2o,
	emissoes_equivalentes_ced=emissoes_equivalentes,
	emissoes_biomassa_ced=emissoes_biomassa
	)
	total.save()
	##############################################################
		
	return render_to_response('ced/resumo_ced.html',{'fossilco2':fossilco2,
													 'fossilch4':fossilch4,
													 'fossiln2o':fossiln2o,
													 'bioch4':bioch4,
													 'bioco2':bioco2,
													 'bion2o':bion2o,
													 'emissoes_equivalentes':emissoes_equivalentes,
													 'emissoes_biomassa':emissoes_biomassa},
													 context_instance=RequestContext(request)) 
			
def lista_ced(request):
	lista_itens=CED.objects.all()
	context=RequestContext(request)
	return render_to_response('ced/lista_ced.html',{'lista_itens':lista_itens},context)

def remove_ced(request,nr_item):
	item=get_object_or_404(CED, pk=nr_item)
	item.delete()
	return render_to_response('ced/lista_ced.html',context_instance=RequestContext(request))

def edita_ced(request,nr_item):
	objeto=CED.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormCED(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('ced/edita_ced.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormCED(instance=objeto)
	return render_to_response('ced/edita_ced.html',{'form':form},context_instance=RequestContext(request))


	


#######################################################################################################################################		
	
def adiciona_fonteCED(request):
	if request.method=='POST':		
		form=FormFonteCED(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('fonteced/add_FonteCED.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteCED()
	return render_to_response('fonteced/add_FonteCED.html',{'form':form},context_instance=RequestContext(request))

def lista_fonteCED(request):
	lista_itens=FonteCED.objects.all()
	context=RequestContext(request)
	return render_to_response('fonteced/lista_fonteCED.html',{'lista_itens':lista_itens},context)
	
def remove_fonteCED(request,nr_item):
	item=get_object_or_404(FonteCED, pk=nr_item)
	item.delete()
	return render_to_response('fonteced/lista_fonteCED.html',context_instance=RequestContext(request))
	
def edita_fonteCED(request,nr_item):
	objeto=FonteCED.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteCED(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonteced/edita_fonteCED.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteCED(instance=objeto)
	return render_to_response('fonteced/edita_fonteCED.html',{'form':form},context_instance=RequestContext(request))

######################################################################################################################################


	

