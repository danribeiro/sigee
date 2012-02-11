# Create your views here.
#-*- coding: utf-8 -*-

from compra_vapor.models import ECV, FonteECV, FonteEmissaoECV, TotalECV
from fonte_emissao.models import FonteEmissao, EfSetor, SetorAtividade
from forms import FormECV, FormFonteECV, FormFonteEmissaoECV
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def adiciona_ecv(request):
	if request.method=='POST':
		form=FormECV(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('ecv/add_ecv.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormECV()				
	return render_to_response('ecv/add_ecv.html',{'form':form},context_instance=RequestContext(request))

def remove_ecv(request,nr_item):
	item=ECV.objects.get(pk=nr_item)
	item.delete()
	return render_to_response('ecv/lista_ecv.html',context_instance=RequestContext(request))	
	
def lista_ecv(request):
	lista_itens=ECV.objects.all()
	return render_to_response('ecv/lista_ecv.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))
	

def calcula_ecv(request,nr_item):
	ecv=get_object_or_404(ECV, pk=nr_item) 
	emissoes=FonteECV.objects.all()
	totalbioch4=totalbion2o=totalbioco2=totalfossilch4=totalfossiln2o=totalfossilco2=emissoes_biomassa=emissoes_equivalentes=0
	for item in emissoes:
		emissao=FonteECV.objects.get(pk=item.id)
		fonte=FonteEmissaoECV.objects.get(pk=emissao.fonte_emissao_id)				
			
		if fonte.tipo==1:#biomassa			
			valor=emissao.fervedor/100			
			parte1=(emissao.vapor/valor)			
			totalbioco2=totalbioco2+((((fonte.fatorco2/fonte.caloria)/fonte.densidade)*1000)*parte1)
			totalbioch4=totalbioch4+((((fonte.fatorch4/fonte.caloria)/fonte.densidade)*1000)*parte1)
			totalbion2o=totalbion2o+((((fonte.fatorn2o/fonte.caloria)/fonte.densidade)*1000)*parte1)
			
	
		elif fonte.tipo==2:#fóssil			
			valor=emissao.fervedor/100	
			parte1=(emissao.vapor/valor)
			
			totalfossilco2=totalfossilco2+((((fonte.fatorco2/fonte.caloria)/fonte.densidade)*1000)*parte1)		
				
			totalfossilch4=totalfossilch4+((((fonte.fatorch4/fonte.caloria)/fonte.densidade)*1000)*parte1)
			
			totalfossiln2o=totalfossiln2o+((((fonte.fatorn2o/fonte.caloria)/fonte.densidade)*1000)*parte1)
			
		
	totalgeralch4=(totalbioch4+totalfossilch4)*21 # GWP CH4 = 21 
	totalgeraln2o=(totalbion2o+totalfossiln2o)*310 # GWP N2O = 310 
	
	 #	
			
	emissoes_equivalentes=(totalfossilco2+ totalgeralch4 + totalgeraln2o)/1000 #calcula o total de emissões equivalentes (toneladas métricas)		
	emissoes_biomassa=totalbioco2/1000 #calcula o total de emissões equivalentes de Biomassa (toneladas metricas)		
		
		
		#truncando os valores para renderização 
	emissoes_biomassa=round(emissoes_biomassa,1)		
	emissoes_equivalentes=round(emissoes_equivalentes,1)	 
	totalfossilco2=round(totalfossilco2,1)
	totalfossilch4=round(totalfossilch4,1)
	totalfossiln2o=round(totalfossiln2o,1)
	totalbioch4=round(totalbioch4,1)
	totalbion2o=round(totalbion2o,1)
	totalbioco2=round(totalbioco2,1)
	
	############################################################################
	#salva os totais na tabela TotalECV
	total=TotalECV(
	ecv=ecv,
	ecv_fossil_co2=totalfossilco2,
	ecv_fossil_ch4=totalfossilch4,
	ecv_fossil_n2o=totalfossiln2o,
	ecv_bio_co2=totalbioco2,
	ecv_bio_ch4=totalbioch4,
	ecv_bio_n2o=totalbion2o,
	ecv_emissoes_equivalentes=emissoes_equivalentes,
	ecv_emissoes_biomassa=emissoes_biomassa
	)
	total.save()
	
	############################################################################
		
	return render_to_response('ecv/resumo_ecv.html',{'totalfossilco2':totalfossilco2,
													 'totalfossilch4':totalfossilch4,
													 'totalfossiln2o':totalfossiln2o,
													 'totalbioch4':totalbioch4,
													 'totalbioco2':totalbioco2,
													 'totalbion2o':totalbion2o,
													 'emissoes_equivalentes':emissoes_equivalentes,
													 'emissoes_biomassa':emissoes_biomassa},
													 context_instance=RequestContext(request))


def edita_ecv(request,nr_item):
	objeto=ECV.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormECV(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('ecv/edita_ecv.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormECV(instance=objeto)
	return render_to_response('ecv/edita_ecv.html',{'form':form},context_instance=RequestContext(request)) 													 
######################################

def adiciona_fonteecv(request):
	if request.method=='POST':
		form=FormFonteECV(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fonteecv/add_fonteecv.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteECV()				
	return render_to_response('fonteecv/add_fonteecv.html',{'form':form},context_instance=RequestContext(request))

def remove_fonteecv(request,nr_item):
	item=FonteECV.objects.get(pk=nr_item)
	item.delete()
	return render_to_response('fonteecv/lista_fonteecv.html',context_instance=RequestContext(request))	
	
def lista_fonteecv(request):
	lista_itens=FonteECV.objects.all()
	return render_to_response('fonteecv/lista_fonteecv.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))

def edita_fonteecv(request,nr_item):
	objeto=FonteECV.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteECV(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonteecv/edita_fonteecv.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteECV(instance=objeto)
	return render_to_response('fonteecv/edita_fonteecv.html',{'form':form},context_instance=RequestContext(request)) 													 
	
##########################################
def adiciona_fonte(request):
	if request.method=='POST':
		form=FormFonteEmissaoECV(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fonteecv/add_fonte.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteEmissaoECV()				
	return render_to_response('fonteecv/add_fonte.html',{'form':form},context_instance=RequestContext(request))

def remove_fonte(request,nr_item):
	item=FonteEmissaoECV.objects.get(pk=nr_item)
	item.delete()
	return render_to_response('fonteecv/lista_fonte.html',context_instance=RequestContext(request))	
	
def lista_fonte(request):
	lista_itens=FonteEmissaoECV.objects.all()
	return render_to_response('fonteecv/lista_fonte.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))

def edita_fonte(request,nr_item):
	objeto=FonteEmissaoECV.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteEmissaoECV(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonteecv/edita_fonte.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteEmissaoECV(instance=objeto)
	return render_to_response('fonteecv/edita_fonte.html',{'form':form},context_instance=RequestContext(request)) 													 
	

