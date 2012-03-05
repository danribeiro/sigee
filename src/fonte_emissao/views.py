# Create your views here.
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from forms import FonteForm, EfSetorForm, SetorForm
from django.http import Http404, HttpResponse
from fonte_emissao.models import FonteEmissao, EfSetor, SetorAtividade
from django.forms.models import inlineformset_factory

#from report import write_to_pdf

#views de adição da tabela de Fontes de Emissão
def adiciona_fonte(request):
	if request.method=='POST':
		form=FonteForm(request.POST,request.FILES)	
		if form.is_valid():
			form.save()			
			return render_to_response('fonte_emissao/adiciona_fonte.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FonteForm()		
	return render_to_response('fonte_emissao/adiciona_fonte.html',{'form':form},context_instance=RequestContext(request))

def remove_fonte(request,nr_item):
	item=get_object_or_404(FonteEmissao, pk=nr_item)
	item.delete()
	return render_to_response('fonte_emissao/lista_fonte.html',context_instance=RequestContext(request))
	
def item(request, nr_item):
	item = get_object_or_404(FonteEmissao, pk=nr_item)
	return render_to_response('fonte_emissao/item_fonte.html',{'item':item},context_instance=RequestContext(request))

def lista_fonte(request):
	lista_itens=FonteEmissao.objects.all()
	context=RequestContext(request)
	return render_to_response('fonte_emissao/lista_fonte.html',{'lista_itens':lista_itens},context)

def edita_fonte(request,nr_item):
	objeto=FonteEmissao.objects.get(pk=nr_item)
	if request.method=='POST':
		form=FonteForm(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('fonte_emissao/edita_fonte.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=FonteForm(instance=objeto)
	return render_to_response('fonte_emissao/edita_fonte.html',{'form':form},context_instance=RequestContext(request))
	
#def gerapdf_fonte(request):
#    fontes = FonteEmissao.objects.all()
    
	
			
#views de edição da tabela de setor de atividades
def adiciona_setor(request):
	if request.method=='POST':
		form=SetorForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('setor/adiciona_setor.html',{'form':form}, context_instance=RequestContext(request))
	else:
		form=SetorForm()		
	return render_to_response('setor/adiciona_setor.html',{'form':form}, context_instance=RequestContext(request) )

def remove_setor(request,nr_item):
	item=get_object_or_404(SetorAtividade, pk=nr_item)
	item.delete()
	return render_to_response('setor/lista_setor.html',context_instance=RequestContext(request))
	
def lista_setor(request):
	lista_itens=SetorAtividade.objects.all()
	return render_to_response('setor/lista_setor.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))

def edita_setor(request,nr_item):
	objeto=SetorAtividade.objects.get(pk=nr_item)
	if request.method=='POST':
		form=SetorForm(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('setor/edita_setor.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=SetorForm(instance=objeto)
	return render_to_response('setor/edita_setor.html',{'form':form},context_instance=RequestContext(request))	
	
		
#views de edição da tabela de Fatores de CH4/N2O por setor de atividade
def adiciona_ef(request):
	if request.method=='POST':
		form=EfSetorForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('efsetor/adiciona_ef.html',{'form':form}, context_instance=RequestContext(request))
	else:
		form=EfSetorForm()		
	return render_to_response('efsetor/adiciona_ef.html',{'form':form}, context_instance=RequestContext(request) )

def remove_ef(request,nr_item):
	item=get_object_or_404(EfSetor, pk=nr_item)
	item.delete()
	return render_to_response('efsetor/lista_ef.html',context_instance=RequestContext(request))
	
def lista_ef(request):
	lista_itens=EfSetor.objects.all()
	return render_to_response('efsetor/lista_ef.html',{'lista_itens':lista_itens},context_instance=RequestContext(request))

def edita_ef(request,nr_item):
	objeto=EfSetor.objects.get(pk=nr_item)
	if request.method=='POST':
		form=EfSetorForm(request.POST,instance=objeto)		
		if form.is_valid():
			form.save()
			return render_to_response('efsetor/edita_ef.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=EfSetorForm(instance=objeto)
	return render_to_response('efsetor/edita_ef.html',{'form':form},context_instance=RequestContext(request))
#######################################################################################################################################





