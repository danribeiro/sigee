# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import FormFonteRAC, FormRAC, FormGas, FormEquipamento
from models import FonteRAC, RAC, Gas, Equipamento, TotalRAC


#viwes que manipulam os objetos da tabela ECM
def adiciona_rac(request):
	if request.method=='POST':
		form=FormRAC(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('rac/add_rac.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormRAC()				
	return render_to_response('rac/add_rac.html',{'form':form},context_instance=RequestContext(request))

def remove_rac(request,nr_item):
	item=RAC.objects.get(pk=nr_item)
	item.delete()
	return render_to_response('rac/lista_rac.html',context_instance=RequestContext(request))	
	
def lista_rac(request):
	lista_itens=RAC.objects.all()
	return render_to_response('rac/lista_rac.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))
	
def calcula_rac(request, nr_item):
	rac=get_object_or_404(RAC, pk=nr_item) 
	emissoes=FonteRAC.objects.all()
	totalco2=0
	for emissao in emissoes:
		item=FonteRAC.objects.get(pk=emissao.id)
		gas=Gas.objects.get(pk=item.gas_rac_id)
		tipo=Equipamento.objects.get(pk=item.equipamento_rac_id)
		novas=tipo.coe_novas
		operacional=tipo.coe_operacional
		dispensado=tipo.coe_dispensado
			
		totalco2=totalco2+((novas*item.novas+operacional*item.operacional+dispensado*item.dispensado)*gas.gwp)
	
		
	emissoes_equivalentes=totalco2/1000
	
	totalco2=round( totalco2,1)
	emissoes_equivalentes=round(emissoes_equivalentes,1)
	
	#######################################################################
	#salvo os totais na tabela TotalRAC
	total=TotalRAC(
	rac=rac,
	totalrac_co2=totalco2,
	emissoes_equivalentes_rac=emissoes_equivalentes
	)	
	total.save()
	#######################################################################
	
	
	return render_to_response('rac/resumo_rac.html',{'emissoes_equivalentes':emissoes_equivalentes,
													 'totalco2':totalco2},
													 context_instance=RequestContext(request))
													 
													 
def edita_rac(request,nr_item):
	objeto=RAC.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormRAC(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('rac/edita_rac.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormRAC(instance=objeto)
	return render_to_response('rac/edita_rac.html',{'form':form},context_instance=RequestContext(request))
	
###############

def adiciona_fonterac(request):
	if request.method=='POST':
		form=FormFonteRAC(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('fonterac/add_fonterac.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteRAC()				
	return render_to_response('fonterac/add_fonterac.html',{'form':form},context_instance=RequestContext(request))
	
def lista_fonterac(request):
	lista_itens=FonteRAC.objects.all()
	context=RequestContext(request)
	return render_to_response('fonterac/lista_fonterac.html',{'lista_itens':lista_itens},context)
	
def remove_fonterac(request,nr_item):
	item=get_object_or_404(FonteRAC, pk=nr_item)
	item.delete()
	return render_to_response('fonterac/lista_fonterac.html',context_instance=RequestContext(request))
	
def edita_fonterac(request,nr_item):
	objeto=FonteRAC.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormFonteRAC(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonterac/edita_fonterac.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormFonteRAC(instance=objeto)
	return render_to_response('fonterac/edita_fonterac.html',{'form':form},context_instance=RequestContext(request))

#############################

	
def adiciona_gas(request):
	if request.method=='POST':
		form=FormGas(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('gas_equip/add_gas.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormGas()				
	return render_to_response('gas_equip/add_gas.html',{'form':form},context_instance=RequestContext(request))
	
def lista_gas(request):
	lista_itens=Gas.objects.all()
	context=RequestContext(request)
	return render_to_response('gas_equip/lista_gas.html',{'lista_itens':lista_itens},context)
	
def remove_gas(request,nr_item):
	item=get_object_or_404(Gas, pk=nr_item)
	item.delete()
	return render_to_response('gas_equip/lista_gas.html',context_instance=RequestContext(request))

def edita_gas(request,nr_item):
	objeto=Gas.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormGas(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('gas_equip/edita_gas.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormGas(instance=objeto)
	return render_to_response('gas_equip/edita_gas.html',{'form':form},context_instance=RequestContext(request))
	
#############################

def adiciona_equip(request):
	if request.method=='POST':
		form=FormEquipamento(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('gas_equip/add_equip.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormEquipamento()				
	return render_to_response('gas_equip/add_equip.html',{'form':form},context_instance=RequestContext(request))
	
def lista_equip(request):
	lista_itens=Equipamento.objects.all()
	context=RequestContext(request)
	return render_to_response('gas_equip/lista_equip.html',{'lista_itens':lista_itens},context)
	
def remove_equip(request,nr_item):
	item=get_object_or_404(Equipamento, pk=nr_item)
	item.delete()
	return render_to_response('gas_equip/lista_equip.html',context_instance=RequestContext(request))

def edita_equip(request,nr_item):
	objeto=Equipamento.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FormEquipamento(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('gas_equip/edita_equip.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FormEquipamento(instance=objeto)
	return render_to_response('gas_equip/edita_equip.html',{'form':form},context_instance=RequestContext(request))

##############################
	

