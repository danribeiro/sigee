# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import FormFonteECE, FormECE 
from models import FonteECE, ECE, TotalECE
from inventario.models import Empresa, CED, Inventario, FonteCED
from combustao_movel.models import FatoresVariaveis, Parametros

#vies que manipulam os objetos da tabela ECM
def adiciona_ece(request):
	if request.method=='POST':
		form=FormECE(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('ece/add_ece.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormECE()				
	return render_to_response('ece/add_ece.html',{'form':form},context_instance=RequestContext(request))

def remove_ece(request,nr_item):
	item=ECE.objects.get(pk=nr_item)
	item.delete()
	return render_to_response('ece/lista_ece.html',context_instance=RequestContext(request))	
	
def lista_ece(request):
	lista_itens=ECE.objects.all()
	return render_to_response('ece/lista_ece.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))
	
def calcula_ece(request,nr_item):
	ece=get_object_or_404(ECE, pk=nr_item) 
	inventario_ano=Inventario.objects.get(pk=ece.id)		
	emissoes=FonteECE.objects.all()		
	
	ano_fatores=FatoresVariaveis.objects.get(ano_param=inventario_ano.ano)
	totalco2=0
	for item in emissoes:		
		fonte=FonteECE.objects.get(pk=item.id)
		fator=Parametros.objects.get(mes=fonte.mes)
	
		
		totalco2=totalco2+(fonte.quantidade*fator.fesin)
	
	#totalco2=round(totalco2,1)
	
	emissoes_equivalentes=totalco2/1000
	
	emissoes_equivalentes=round(emissoes_equivalentes,2)
	
	########################################################################
	#salva os totais na tabela TotalECE
	total=TotalECE(
	ece=ece,
	ece_fossil_co2=totalco2,
	ece_emissoes_equivalentes=emissoes_equivalentes
	)
	total.save()
	#######################################################################
	
	return render_to_response('ece/resumo_ece.html',{'emissoes_equivalentes':emissoes_equivalentes,
													 'totalco2':totalco2},
													 context_instance=RequestContext(request))

def edita_ece(request,nr_item):
	objeto=ECE.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormECE(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('ece/edita_ece.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormECE(instance=objeto)
	return render_to_response('ece/edita_ece.html',{'form':form},context_instance=RequestContext(request))

#######################

def adiciona_fonteece(request):
	if request.method=='POST':
		form=FormFonteECE(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fonteece/add_fonteece.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteECE()				
	return render_to_response('fonteece/add_fonteece.html',{'form':form},context_instance=RequestContext(request))
	
def lista_fonteece(request):
	lista_itens=FonteECE.objects.all()
	context=RequestContext(request)
	return render_to_response('fonteece/lista_fonteece.html',{'lista_itens':lista_itens},context)
	
def remove_fonteece(request,nr_item):
	item=get_object_or_404(FonteECE, pk=nr_item)
	item.delete()
	return render_to_response('fonteece/lista_fonteece.html',context_instance=RequestContext(request))

def edita_fonteece(request,nr_item):
	objeto=FonteECE.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteECE(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonteece/edita_fonteece.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteECE(instance=objeto)
	return render_to_response('fonteece/edita_fonteece.html',{'form':form},context_instance=RequestContext(request))
	
#########################




	


