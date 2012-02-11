# Create your views here.
#-*-coding:utf-8 -*-

from django.shortcuts import render_to_response,HttpResponse
from django.template import RequestContext
#from django.Http import 
from inventario.models import *
from combustao_movel.models import *
from compra_vapor.models import *
from compra_energia.models import *
from emissao_rac.models import *

from inventario.views import *
from combustao_movel.views import *
from compra_vapor.views import *
from compra_energia.views import *
from emissao_rac.views import *

from report import write_to_pdf
import cairo
import CairoPlot

from CairoPlot import bar_plot
import pdb
from combustao_movel.models import FonteECM

	
def calcula_resumo(request):
	inventario=Inventario.objects.get()
	empresa=Empresa.objects.get(inventario=inventario)#get da empresa
	nome_empresa=empresa.nome
	rua_empresa=empresa.rua
	numero_empresa=empresa.numero
	bairro_empresa=empresa.bairro
	cep_empresa=empresa.cep
	cidade_empresa=empresa.cidade
	estado_empresa=empresa.estado
	inventario=inventario.ano #ano do inventário	
	
	#ced=CED.objects.get(inventario=inventario)
	#rac=RAC.objects.get(inventario=inventario)
	#ecv=ECV.objects.get(inventario=inventario)
	#ece=ECE.objects.get(inventario=inventario)
	#ecm=ECM.objects.get(inventario=inventario)
	
	totalecv=TotalECV.objects.all() #busca totais de ECM salvos 
	countecv=totalecv.count()	#atualiza o numero do id 
	
	totalece=TotalECE.objects.all() #busca totais de ECE salvos 
	countece=totalece.count()	#atualiza o numero do id
	
	totalecm=TotalECM.objects.all() #busca totais de ECV salvos 
	countecm=totalecm.count()	#atualiza o numero do id
	
	totalced=TotalCED.objects.all() #busca totais de CED salvos 
	countced=totalced.count()	#atualiza o numero do id
	
	totalrac=TotalRAC.objects.all() #busca totais de RAC salvos 
	countrac=totalrac.count()	#atualiza o numero do id 	
	
	
	#############################################################################
	
	 
	if totalced.exists() or totalrac.exists() or totalecm.exists() or totalece.exists() or totalecv.exists():
		#totais de CED
		totalced=TotalCED.objects.get(pk=countced) #pega o objeto mais atual
		ced_fossil_co2=totalced.fossilced_co2
		ced_fossil_ch4=totalced.fossilced_ch4
		ced_fossil_n2o=totalced.fossilced_n2o				
		ced_bioco2=totalced.bioced_co2
		ced_bioch4=totalced.bioced_ch4
		ced_bion2o=totalced.bioced_n2o
		ced_emissoes_equivalentes=totalced.emissoes_equivalentes_ced
		ced_emissoes_biomassa=totalced.emissoes_biomassa_ced
		
			
	############################################################################	
	
		totalrac=TotalRAC.objects.get(pk=countrac)
		rac_total_co2=totalrac.totalrac_co2
		rac_emissoes_equivalentes=totalrac.emissoes_equivalentes_rac
		
	############################################################################	
		
		totalecm=TotalECM.objects.get(pk=countecm)
		ecm_fossil_co2=totalecm.ecm_fossil_co2
		ecm_bio_co2=totalecm.ecm_bio_co2		
		ecm_emissoes_equivalentes=totalecm.ecm_emissoes_equivalentes
		ecm_emissoes_biomassa=totalecm.ecm_emissoes_biomassa
		
	############################################################################
	
		totalece=TotalECE.objects.get(pk=countece)
		ece_fossil_co2=totalece.ece_fossil_co2
		ece_emissoes_equivalentes=totalece.ece_emissoes_equivalentes
		
	############################################################################
	
		totalecv=TotalECV.objects.get(pk=countecv)
		ecv_fossil_co2=totalecv.ecv_fossil_co2
		ecv_fossil_ch4=totalecv.ecv_fossil_ch4
		ecv_fossil_n2o=totalecv.ecv_fossil_n2o
		ecv_bio_co2=totalecv.ecv_bio_co2
		ecv_bio_ch4=totalecv.ecv_bio_ch4
		ecv_bio_n2o=totalecv.ecv_bio_n2o
		ecv_emissoes_equivalentes=totalecv.ecv_emissoes_equivalentes
		ecv_emissoes_biomassa=totalecv.ecv_emissoes_biomassa
	
	############################################################################
	
	
		total_emissoes_equivalentes_co2=ced_fossil_co2+ecm_fossil_co2+ecv_fossil_co2+rac_total_co2+ece_fossil_co2
	
		total_emissoes_biomassa_co2=ecv_bio_co2+ecm_bio_co2+ecv_bio_co2
	
		total_equivalente_ch4=ced_fossil_ch4+ecv_fossil_ch4
		total_equivalente_n2o=ced_fossil_n2o+ecv_fossil_n2o
	
		total_geral_equivalentes=ced_emissoes_equivalentes+ecv_emissoes_equivalentes+ecm_emissoes_equivalentes+ece_emissoes_equivalentes+rac_emissoes_equivalentes
	
		total_geral_biomassa=ecv_emissoes_biomassa+ced_emissoes_biomassa+ecm_emissoes_biomassa
		
			
		return render_to_response('resumo/pagina_resumo.html', {
		#dados de CED 
		'ced_fossil_co2':ced_fossil_co2,'ced_fossil_ch4':ced_fossil_ch4,'ced_fossil_n2o':ced_fossil_n2o,'ced_emissoes_equivalentes':ced_emissoes_equivalentes,
		'ced_emissoes_biomassa':ced_emissoes_biomassa,'ced_bioco2':ced_bioco2,'ced_bioch4':ced_bioch4,'ced_bion2o':ced_bion2o,
		
		#dados da empresa
		'inventario':inventario,'nome_empresa':nome_empresa,'rua_empresa':rua_empresa,'numero_empresa':numero_empresa,'bairro_empresa':bairro_empresa,
		'cep_empresa':cep_empresa, 'cidade_empresa':cidade_empresa, 'estado_empresa':estado_empresa,
		
		#dados de RAC
		'rac_total_co2':rac_total_co2,'rac_emissoes_equivalentes':rac_emissoes_equivalentes,
		
		#dados de ECM
		'ecm_fossil_co2':ecm_fossil_co2,'ecm_emissoes_equivalentes':ecm_emissoes_equivalentes,'ecm_emissoes_biomassa':ecm_emissoes_biomassa,'ecm_bio_co2':ecm_bio_co2,
		
		#dados de ECE
		'ece_fossil_co2':ece_fossil_co2,'ece_emissoes_equivalentes':ece_emissoes_equivalentes,
		
		#dados de ECV
		'ecv_fossil_co2':ecv_fossil_co2,'ecv_fossil_ch4':ecv_fossil_ch4, 'ecv_fossil_n2o':ecv_fossil_n2o,'ecv_emissoes_equivalentes':ecv_emissoes_equivalentes,'ecv_emissoes_biomassa':ecv_emissoes_biomassa,'ecv_bio_co2':ecv_bio_co2,
		#############################################################################################################################
		#total de CH4 e N2O
		'total_equivalente_ch4':total_equivalente_ch4,'total_equivalente_n2o':total_equivalente_n2o,		
		
		#total de emissoes relativos a CO2
		'total_emissoes_equivalentes_co2':total_emissoes_equivalentes_co2,
		
		#total de emissoes biomassa relativos a CO2
		'total_emissoes_biomassa_co2':total_emissoes_biomassa_co2,
		
		#total geral de emissoes CO2 equivalente
		'total_geral_equivalentes':total_geral_equivalentes,
		
		#total geral de emissoes CO2 biomassa
		'total_geral_biomassa':total_geral_biomassa,
		
		},context_instance=RequestContext(request))
	else:
	
		return render_to_response('resumo/pagina_resumo.html',{},context_instance=RequestContext(request))
	
		
		
def relatorio_resumo(request):
	inventario=Inventario.objects.get()
	empresa=Empresa.objects.get(inventario=inventario)#get da empresa
	nome_empresa=empresa.nome
	rua_empresa=empresa.rua
	numero_empresa=empresa.numero
	bairro_empresa=empresa.bairro
	cep_empresa=empresa.cep
	cidade_empresa=empresa.cidade
	estado_empresa=empresa.estado
	inventario=inventario.ano #ano do inventário	
	
	#ced=CED.objects.get(inventario=inventario)
	#rac=RAC.objects.get(inventario=inventario)
	#ecv=ECV.objects.get(inventario=inventario)
	#ece=ECE.objects.get(inventario=inventario)
	#ecm=ECM.objects.get(inventario=inventario)
	
	totalecv=TotalECV.objects.all() #busca totais de ECM salvos 
	countecv=totalecv.count()	#atualiza o numero do id 
	
	totalece=TotalECE.objects.all() #busca totais de ECE salvos 
	countece=totalece.count()	#atualiza o numero do id
	
	totalecm=TotalECM.objects.all() #busca totais de ECV salvos 
	countecm=totalecm.count()	#atualiza o numero do id
	
	totalced=TotalCED.objects.all() #busca totais de CED salvos 
	countced=totalced.count()	#atualiza o numero do id
	
	totalrac=TotalRAC.objects.all() #busca totais de RAC salvos 
	countrac=totalrac.count()	#atualiza o numero do id 	
	
	
	#############################################################################
	
	 
	if totalced.exists() or totalrac.exists() or totalecm.exists() or totalece.exists() or totalecv.exists():
		#totais de CED
		totalced=TotalCED.objects.get(pk=countced) #pega o objeto mais atual
		ced_fossil_co2=totalced.fossilced_co2
		ced_fossil_ch4=totalced.fossilced_ch4
		ced_fossil_n2o=totalced.fossilced_n2o				
		ced_bioco2=totalced.bioced_co2
		ced_bioch4=totalced.bioced_ch4
		ced_bion2o=totalced.bioced_n2o
		ced_emissoes_equivalentes=totalced.emissoes_equivalentes_ced
		ced_emissoes_biomassa=totalced.emissoes_biomassa_ced
		
			
	############################################################################	
	
		totalrac=TotalRAC.objects.get(pk=countrac)
		rac_total_co2=totalrac.totalrac_co2
		rac_emissoes_equivalentes=totalrac.emissoes_equivalentes_rac
		
	############################################################################	
		
		totalecm=TotalECM.objects.get(pk=countecm)
		ecm_fossil_co2=totalecm.ecm_fossil_co2
		ecm_bio_co2=totalecm.ecm_bio_co2		
		ecm_emissoes_equivalentes=totalecm.ecm_emissoes_equivalentes
		ecm_emissoes_biomassa=totalecm.ecm_emissoes_biomassa
		
	############################################################################
	
		totalece=TotalECE.objects.get(pk=countece)
		ece_fossil_co2=totalece.ece_fossil_co2
		ece_emissoes_equivalentes=totalece.ece_emissoes_equivalentes
		
	############################################################################
	
		totalecv=TotalECV.objects.get(pk=countecv)
		ecv_fossil_co2=totalecv.ecv_fossil_co2
		ecv_fossil_ch4=totalecv.ecv_fossil_ch4
		ecv_fossil_n2o=totalecv.ecv_fossil_n2o
		ecv_bio_co2=totalecv.ecv_bio_co2
		ecv_bio_ch4=totalecv.ecv_bio_ch4
		ecv_bio_n2o=totalecv.ecv_bio_n2o
		ecv_emissoes_equivalentes=totalecv.ecv_emissoes_equivalentes
		ecv_emissoes_biomassa=totalecv.ecv_emissoes_biomassa
	
	############################################################################
	
	
		total_emissoes_equivalentes_co2=ced_fossil_co2+ecm_fossil_co2+ecv_fossil_co2+rac_total_co2+ece_fossil_co2
	
		total_emissoes_biomassa_co2=ecv_bio_co2+ecm_bio_co2+ecv_bio_co2
	
		total_equivalente_ch4=ced_fossil_ch4+ecv_fossil_ch4
		total_equivalente_n2o=ced_fossil_n2o+ecv_fossil_n2o
	
		total_geral_equivalentes=ced_emissoes_equivalentes+ecv_emissoes_equivalentes+ecm_emissoes_equivalentes+ece_emissoes_equivalentes+rac_emissoes_equivalentes
	
		total_geral_biomassa=ecv_emissoes_biomassa+ced_emissoes_biomassa
		
		return write_to_pdf('resumo/relatorio_resumo.html', 			
		{
		#dados de CED 
		'ced_fossil_co2':ced_fossil_co2,'ced_fossil_ch4':ced_fossil_ch4,'ced_fossil_n2o':ced_fossil_n2o,'ced_emissoes_equivalentes':ced_emissoes_equivalentes,
		'ced_emissoes_biomassa':ced_emissoes_biomassa,'ced_bioco2':ced_bioco2,'ced_bioch4':ced_bioch4,'ced_bion2o':ced_bion2o,
		
		#dados da empresa
		'inventario':inventario,'nome_empresa':nome_empresa,'rua_empresa':rua_empresa,'numero_empresa':numero_empresa,'bairro_empresa':bairro_empresa,
		'cep_empresa':cep_empresa, 'cidade_empresa':cidade_empresa, 'estado_empresa':estado_empresa,
		
		#dados de RAC
		'rac_total_co2':rac_total_co2,'rac_emissoes_equivalentes':rac_emissoes_equivalentes,
		
		#dados de ECM
		'ecm_fossil_co2':ecm_fossil_co2,'ecm_emissoes_equivalentes':ecm_emissoes_equivalentes,'ecm_emissoes_biomassa':ecm_emissoes_biomassa,'ecm_bio_co2':ecm_bio_co2,
		
		#dados de ECE
		'ece_fossil_co2':ece_fossil_co2,'ece_emissoes_equivalentes':ece_emissoes_equivalentes,
		
		#dados de ECV
		'ecv_fossil_co2':ecv_fossil_co2,'ecv_fossil_ch4':ecv_fossil_ch4, 'ecv_fossil_n2o':ecv_fossil_n2o,'ecv_emissoes_equivalentes':ecv_emissoes_equivalentes,'ecv_emissoes_biomassa':ecv_emissoes_biomassa,'ecv_bio_co2':ecv_bio_co2,
		#############################################################################################################################
		#total de CH4 e N2O
		'total_equivalente_ch4':total_equivalente_ch4,'total_equivalente_n2o':total_equivalente_n2o,		
		
		#total de emissoes relativos a CO2
		'total_emissoes_equivalentes_co2':total_emissoes_equivalentes_co2,
		
		#total de emissoes biomassa relativos a CO2
		'total_emissoes_biomassa_co2':total_emissoes_biomassa_co2,
		
		#total geral de emissoes CO2 equivalente
		'total_geral_equivalentes':total_geral_equivalentes,
		
		#total geral de emissoes CO2 biomassa
		'total_geral_biomassa':total_geral_biomassa,
		
		},'Relatório')
	

def gen_graph(request):
	
	inventario=Inventario.objects.get()
	empresa=Empresa.objects.get(inventario=inventario)#get da empresa
	nome_empresa=empresa.nome
	rua_empresa=empresa.rua
	numero_empresa=empresa.numero
	bairro_empresa=empresa.bairro
	cep_empresa=empresa.cep
	cidade_empresa=empresa.cidade
	estado_empresa=empresa.estado
	inventario=inventario.ano #ano do
	
	totalecv=TotalECV.objects.all() #busca totais de ECM salvos 
	countecv=totalecv.count()	#atualiza o numero do id 
	
	totalece=TotalECE.objects.all() #busca totais de ECE salvos 
	countece=totalece.count()	#atualiza o numero do id
	
	totalecm=TotalECM.objects.all() #busca totais de ECV salvos 
	countecm=totalecm.count()	#atualiza o numero do id
	
	totalced=TotalCED.objects.all() #busca totais de CED salvos 
	countced=totalced.count()	#atualiza o numero do id
	
	totalrac=TotalRAC.objects.all() #busca totais de RAC salvos 
	countrac=totalrac.count()	#atualiza o numero do id 	
	
	
	#############################################################################
	
	 
	if totalced.exists() or totalrac.exists() or totalecm.exists() or totalece.exists() or totalecv.exists():
		#totais de CED
		totalced=TotalCED.objects.get(pk=countced) #pega o objeto mais atual
		ced_fossil_co2=totalced.fossilced_co2
		ced_fossil_ch4=totalced.fossilced_ch4
		ced_fossil_n2o=totalced.fossilced_n2o				
		ced_bioco2=totalced.bioced_co2
		ced_bioch4=totalced.bioced_ch4
		ced_bion2o=totalced.bioced_n2o
		ced_emissoes_equivalentes=totalced.emissoes_equivalentes_ced
		ced_emissoes_biomassa=totalced.emissoes_biomassa_ced
		
			
	############################################################################	
	
		totalrac=TotalRAC.objects.get(pk=countrac)
		rac_total_co2=totalrac.totalrac_co2
		rac_emissoes_equivalentes=totalrac.emissoes_equivalentes_rac
		
	############################################################################	
		
		totalecm=TotalECM.objects.get(pk=countecm)
		ecm_fossil_co2=totalecm.ecm_fossil_co2
		ecm_bio_co2=totalecm.ecm_bio_co2		
		ecm_emissoes_equivalentes=totalecm.ecm_emissoes_equivalentes
		ecm_emissoes_biomassa=totalecm.ecm_emissoes_biomassa
		
	############################################################################
	
		totalece=TotalECE.objects.get(pk=countece)
		ece_fossil_co2=totalece.ece_fossil_co2
		ece_emissoes_equivalentes=totalece.ece_emissoes_equivalentes
		
	############################################################################
	
		totalecv=TotalECV.objects.get(pk=countecv)
		ecv_fossil_co2=totalecv.ecv_fossil_co2
		ecv_fossil_ch4=totalecv.ecv_fossil_ch4
		ecv_fossil_n2o=totalecv.ecv_fossil_n2o
		ecv_bio_co2=totalecv.ecv_bio_co2
		ecv_bio_ch4=totalecv.ecv_bio_ch4
		ecv_bio_n2o=totalecv.ecv_bio_n2o
		ecv_emissoes_equivalentes=totalecv.ecv_emissoes_equivalentes
		ecv_emissoes_biomassa=totalecv.ecv_emissoes_biomassa
	
	############################################################################
	
	
		total_emissoes_equivalentes_co2=ced_fossil_co2+ecm_fossil_co2+ecv_fossil_co2+rac_total_co2+ece_fossil_co2
	
		total_emissoes_biomassa_co2=ecv_bio_co2+ecm_bio_co2+ecv_bio_co2
	
		total_equivalente_ch4=ced_fossil_ch4+ecv_fossil_ch4
		total_equivalente_n2o=ced_fossil_n2o+ecv_fossil_n2o
	
		total_geral_equivalentes=ced_emissoes_equivalentes+ecv_emissoes_equivalentes+ecm_emissoes_equivalentes+ece_emissoes_equivalentes+rac_emissoes_equivalentes
	
		total_geral_biomassa=ecv_emissoes_biomassa+ced_emissoes_biomassa

		
		heigth = 700
	   	width = 400			
		data=[ced_emissoes_equivalentes, ecm_emissoes_equivalentes, rac_emissoes_equivalentes, ece_emissoes_equivalentes, ecv_emissoes_equivalentes,]
		
		if data==[0.0,0.0,0.0,0.0,0.0]:			
			msg="Totais sem números relevantes, reveja os cálculos!"
			return render_to_response('resumo/pagina_resumo.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			v_labels = ["Emissões Escopos 1 e 2","CO2-e(toneladas métricas)"]
			h_labels = ["Estacionária", "Móvel", "R&AC", "Energia elétrica","Vapor"]
		   
		   	pp = CairoPlot.BarPlot("grafico.png", data, heigth, width, background = None, border = 20, grid = True, rounded_corners = True, h_labels=h_labels, v_labels=v_labels) 
		   	pp.render()
		   	response = HttpResponse(mimetype="image/png")
		   	pp.surface.write_to_png(response)
		   	return response

def gen_graph_bio(request):
	inventario=Inventario.objects.get()
	empresa=Empresa.objects.get(inventario=inventario)#get da empresa
	nome_empresa=empresa.nome
	rua_empresa=empresa.rua
	numero_empresa=empresa.numero
	bairro_empresa=empresa.bairro
	cep_empresa=empresa.cep
	cidade_empresa=empresa.cidade
	estado_empresa=empresa.estado
	inventario=inventario.ano #ano do
	
	
	totalecv=TotalECV.objects.all() #busca totais de ECM salvos 
	countecv=totalecv.count()	#atualiza o numero do id 
	
	totalece=TotalECE.objects.all() #busca totais de ECE salvos 
	countece=totalece.count()	#atualiza o numero do id
	
	totalecm=TotalECM.objects.all() #busca totais de ECV salvos 
	countecm=totalecm.count()	#atualiza o numero do id
	
	totalced=TotalCED.objects.all() #busca totais de CED salvos 
	countced=totalced.count()	#atualiza o numero do id
	
	totalrac=TotalRAC.objects.all() #busca totais de RAC salvos 
	countrac=totalrac.count()	#atualiza o numero do id 	
	
	
	#############################################################################
	
	 
	if totalced.exists() or totalrac.exists() or totalecm.exists() or totalece.exists() or totalecv.exists():
		#totais de CED
		totalced=TotalCED.objects.get(pk=countced) #pega o objeto mais atual
		ced_fossil_co2=totalced.fossilced_co2
		ced_fossil_ch4=totalced.fossilced_ch4
		ced_fossil_n2o=totalced.fossilced_n2o				
		ced_bioco2=totalced.bioced_co2
		ced_bioch4=totalced.bioced_ch4
		ced_bion2o=totalced.bioced_n2o
		ced_emissoes_equivalentes=totalced.emissoes_equivalentes_ced
		ced_emissoes_biomassa=totalced.emissoes_biomassa_ced
		
			
	############################################################################	
	
		totalrac=TotalRAC.objects.get(pk=countrac)
		rac_total_co2=totalrac.totalrac_co2
		rac_emissoes_equivalentes=totalrac.emissoes_equivalentes_rac
		
	############################################################################	
		
		totalecm=TotalECM.objects.get(pk=countecm)
		ecm_fossil_co2=totalecm.ecm_fossil_co2
		ecm_bio_co2=totalecm.ecm_bio_co2		
		ecm_emissoes_equivalentes=totalecm.ecm_emissoes_equivalentes
		ecm_emissoes_biomassa=totalecm.ecm_emissoes_biomassa
		
	############################################################################
	
		totalece=TotalECE.objects.get(pk=countece)
		ece_fossil_co2=totalece.ece_fossil_co2
		ece_emissoes_equivalentes=totalece.ece_emissoes_equivalentes
		
	############################################################################
	
		totalecv=TotalECV.objects.get(pk=countecv)
		ecv_fossil_co2=totalecv.ecv_fossil_co2
		ecv_fossil_ch4=totalecv.ecv_fossil_ch4
		ecv_fossil_n2o=totalecv.ecv_fossil_n2o
		ecv_bio_co2=totalecv.ecv_bio_co2
		ecv_bio_ch4=totalecv.ecv_bio_ch4
		ecv_bio_n2o=totalecv.ecv_bio_n2o
		ecv_emissoes_equivalentes=totalecv.ecv_emissoes_equivalentes
		ecv_emissoes_biomassa=totalecv.ecv_emissoes_biomassa
	
	############################################################################
	
	
		total_emissoes_equivalentes_co2=ced_fossil_co2+ecm_fossil_co2+ecv_fossil_co2+rac_total_co2+ece_fossil_co2
	
		total_emissoes_biomassa_co2=ecv_bio_co2+ecm_bio_co2+ecv_bio_co2
	
		total_equivalente_ch4=ced_fossil_ch4+ecv_fossil_ch4
		total_equivalente_n2o=ced_fossil_n2o+ecv_fossil_n2o
	
		total_geral_equivalentes=ced_emissoes_equivalentes+ecv_emissoes_equivalentes+ecm_emissoes_equivalentes+ece_emissoes_equivalentes+rac_emissoes_equivalentes
	
		total_geral_biomassa=ecv_emissoes_biomassa+ced_emissoes_biomassa
		
		heigth = 800
	   	width = 400		
		data=[ced_emissoes_biomassa, ecm_emissoes_biomassa, ecv_emissoes_biomassa,]

		if data==[0.0,0.0,0.0]:
			#return HttpResponse('erro')		
			msg="Totais de biomassa sem números relevantes, reveja os cálculos!"
			return render_to_response('resumo/pagina_resumo.html',{'ced_fossil_co2':ced_fossil_co2,'ced_fossil_ch4':ced_fossil_ch4,'ced_fossil_n2o':ced_fossil_n2o,'ced_emissoes_equivalentes':ced_emissoes_equivalentes,
		'ced_emissoes_biomassa':ced_emissoes_biomassa,'ced_bioco2':ced_bioco2,'ced_bioch4':ced_bioch4,'ced_bion2o':ced_bion2o,
		
		#dados da empresa
		'inventario':inventario,'nome_empresa':nome_empresa,'rua_empresa':rua_empresa,'numero_empresa':numero_empresa,'bairro_empresa':bairro_empresa,
		'cep_empresa':cep_empresa, 'cidade_empresa':cidade_empresa, 'estado_empresa':estado_empresa,
		
		#dados de RAC
		'rac_total_co2':rac_total_co2,'rac_emissoes_equivalentes':rac_emissoes_equivalentes,
		
		#dados de ECM
		'ecm_fossil_co2':ecm_fossil_co2,'ecm_emissoes_equivalentes':ecm_emissoes_equivalentes,'ecm_emissoes_biomassa':ecm_emissoes_biomassa,'ecm_bio_co2':ecm_bio_co2,
		
		#dados de ECE
		'ece_fossil_co2':ece_fossil_co2,'ece_emissoes_equivalentes':ece_emissoes_equivalentes,
		
		#dados de ECV
		'ecv_fossil_co2':ecv_fossil_co2,'ecv_fossil_ch4':ecv_fossil_ch4, 'ecv_fossil_n2o':ecv_fossil_n2o,'ecv_emissoes_equivalentes':ecv_emissoes_equivalentes,'ecv_emissoes_biomassa':ecv_emissoes_biomassa,'ecv_bio_co2':ecv_bio_co2,
		#############################################################################################################################
		#total de CH4 e N2O
		'total_equivalente_ch4':total_equivalente_ch4,'total_equivalente_n2o':total_equivalente_n2o,		
		
		#total de emissoes relativos a CO2
		'total_emissoes_equivalentes_co2':total_emissoes_equivalentes_co2,
		
		#total de emissoes biomassa relativos a CO2
		'total_emissoes_biomassa_co2':total_emissoes_biomassa_co2,
		
		#total geral de emissoes CO2 equivalente
		'total_geral_equivalentes':total_geral_equivalentes,
		
		#total geral de emissoes CO2 biomassa
		'total_geral_biomassa':total_geral_biomassa,'msg':msg},context_instance=RequestContext(request))
						
		else:			
			#v_labels = ["CO2-e(toneladas métricas)","500","1000","1500","2000","2500"]
			h_labels = ["Biomassa Estacionária", "Biomassa Móvel", "Biomassa Vapor"]
			v_labels = ["Emissões de Biomassa","CO2-e(toneladas métricas)"]
		   
		   	pp = CairoPlot.BarPlot("gbiomassa.png", data, heigth, width, background = None, border = 20, grid = True, rounded_corners = True, h_labels=h_labels,v_labels=v_labels) 
		   	pp.render()
		   	response = HttpResponse(mimetype="image/png")
		   	pp.surface.write_to_png(response)
		   	return response


def gen_graph_movel(request):
	inventario=Inventario.objects.get()
	empresa=Empresa.objects.get(inventario=inventario)#get da empresa
	nome_empresa=empresa.nome
	rua_empresa=empresa.rua
	numero_empresa=empresa.numero
	bairro_empresa=empresa.bairro
	cep_empresa=empresa.cep
	cidade_empresa=empresa.cidade
	estado_empresa=empresa.estado
	inventario=inventario.ano #ano do
	
	
	totalecv=TotalECV.objects.all() #busca totais de ECM salvos 
	countecv=totalecv.count()	#atualiza o numero do id 
	
	totalece=TotalECE.objects.all() #busca totais de ECE salvos 
	countece=totalece.count()	#atualiza o numero do id
	
	totalecm=TotalECM.objects.all() #busca totais de ECV salvos 
	countecm=totalecm.count()	#atualiza o numero do id
	
	totalced=TotalCED.objects.all() #busca totais de CED salvos 
	countced=totalced.count()	#atualiza o numero do id
	
	totalrac=TotalRAC.objects.all() #busca totais de RAC salvos 
	countrac=totalrac.count()	#atualiza o numero do id 	
	
	
	#############################################################################
	
	 
	if totalced.exists() or totalrac.exists() or totalecm.exists() or totalece.exists() or totalecv.exists():
		#totais de CED
		totalced=TotalCED.objects.get(pk=countced) #pega o objeto mais atual
		ced_fossil_co2=totalced.fossilced_co2
		ced_fossil_ch4=totalced.fossilced_ch4
		ced_fossil_n2o=totalced.fossilced_n2o				
		ced_bioco2=totalced.bioced_co2
		ced_bioch4=totalced.bioced_ch4
		ced_bion2o=totalced.bioced_n2o
		ced_emissoes_equivalentes=totalced.emissoes_equivalentes_ced
		ced_emissoes_biomassa=totalced.emissoes_biomassa_ced
		
			
	############################################################################	
	
		totalrac=TotalRAC.objects.get(pk=countrac)
		rac_total_co2=totalrac.totalrac_co2
		rac_emissoes_equivalentes=totalrac.emissoes_equivalentes_rac
		
	############################################################################	
		
		totalecm=TotalECM.objects.get(pk=countecm)
		ecm_fossil_co2=totalecm.ecm_fossil_co2
		ecm_bio_co2=totalecm.ecm_bio_co2		
		ecm_emissoes_equivalentes=totalecm.ecm_emissoes_equivalentes
		ecm_emissoes_biomassa=totalecm.ecm_emissoes_biomassa
		
	############################################################################
	
		totalece=TotalECE.objects.get(pk=countece)
		ece_fossil_co2=totalece.ece_fossil_co2
		ece_emissoes_equivalentes=totalece.ece_emissoes_equivalentes
		
	############################################################################
	
		totalecv=TotalECV.objects.get(pk=countecv)
		ecv_fossil_co2=totalecv.ecv_fossil_co2
		ecv_fossil_ch4=totalecv.ecv_fossil_ch4
		ecv_fossil_n2o=totalecv.ecv_fossil_n2o
		ecv_bio_co2=totalecv.ecv_bio_co2
		ecv_bio_ch4=totalecv.ecv_bio_ch4
		ecv_bio_n2o=totalecv.ecv_bio_n2o
		ecv_emissoes_equivalentes=totalecv.ecv_emissoes_equivalentes
		ecv_emissoes_biomassa=totalecv.ecv_emissoes_biomassa
	
	############################################################################
	
	
		total_emissoes_equivalentes_co2=ced_fossil_co2+ecm_fossil_co2+ecv_fossil_co2+rac_total_co2+ece_fossil_co2
	
		total_emissoes_biomassa_co2=ecv_bio_co2+ecm_bio_co2+ecv_bio_co2
	
		total_equivalente_ch4=ced_fossil_ch4+ecv_fossil_ch4
		total_equivalente_n2o=ced_fossil_n2o+ecv_fossil_n2o
	
		total_geral_equivalentes=ced_emissoes_equivalentes+ecv_emissoes_equivalentes+ecm_emissoes_equivalentes+ece_emissoes_equivalentes+rac_emissoes_equivalentes
	
		total_geral_biomassa=ecv_emissoes_biomassa+ced_emissoes_biomassa
		totalmes1=totalmes2=totalmes3=totalmes4=totalmes5=totalmes6=totalmes7=totalmes8=totalmes9=totalmes10=totalmes11=totalmes12=0
		emissoesmovel=FonteECM.objects.all()
		if emissoesmovel.exists():
			#count=emissoesmovel.count()
			#return HttpResponse("count =%d" %count)]
			mes1=FonteECM.objects.filter(mes=1)
			mes2=FonteECM.objects.filter(mes=2)
			mes3=FonteECM.objects.filter(mes=3)
			mes4=FonteECM.objects.filter(mes=4)
			mes5=FonteECM.objects.filter(mes=5)
			mes6=FonteECM.objects.filter(mes=6)
			mes7=FonteECM.objects.filter(mes=7)
			mes8=FonteECM.objects.filter(mes=8)
			mes9=FonteECM.objects.filter(mes=9)
			mes10=FonteECM.objects.filter(mes=10)
			mes11=FonteECM.objects.filter(mes=11)
			mes12=FonteECM.objects.filter(mes=12)

			for emissao in mes1:
				totalmes1+=emissao.quantidade
			for emissao in mes2:
				totalmes2+=emissao.quantidade
			for emissao in mes3:
				totalmes3+=emissao.quantidade
			for emissao in mes4:
				totalmes4+=emissao.quantidade
			for emissao in mes5:
				totalmes5+=emissao.quantidade
			for emissao in mes6:
				totalmes6+=emissao.quantidade
			for emissao in mes7:
				totalmes7+=emissao.quantidade
			for emissao in mes8:
				totalmes8+=emissao.quantidade
			for emissao in mes9:
				totalmes9+=emissao.quantidade
			for emissao in mes10:
				totalmes10+=emissao.quantidade
			for emissao in mes11:
				totalmes11+=emissao.quantidade
			for emissao in mes12:
				totalmes12+=emissao.quantidade
			
			heigth = 800
			width = 400		
			data=[totalmes1,totalmes2,totalmes3,totalmes4,totalmes5,totalmes6,totalmes7,totalmes8,totalmes9,totalmes10,totalmes11,totalmes12,]
			v_labels = ["Combustão Móvel","CO2-e(toneladas métricas)"]
			h_labels = ["Janeiro", "Fevereiro", "Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]		   
			pp = CairoPlot.BarPlot("gmovel.png", data, heigth, width, background = None, border = 20, grid = True, rounded_corners = True, h_labels=h_labels,v_labels=v_labels) 
			pp.render()
			response = HttpResponse(mimetype="image/png")
			pp.surface.write_to_png(response)
			return response
	else:
		msg2="sem números relevantes, reveja os cálculos!"
		return render_to_response('resumo/pagina_resumo.html',{'ced_fossil_co2':ced_fossil_co2,'ced_fossil_ch4':ced_fossil_ch4,'ced_fossil_n2o':ced_fossil_n2o,'ced_emissoes_equivalentes':ced_emissoes_equivalentes,
		'ced_emissoes_biomassa':ced_emissoes_biomassa,'ced_bioco2':ced_bioco2,'ced_bioch4':ced_bioch4,'ced_bion2o':ced_bion2o,
		
		#dados da empresa
		'inventario':inventario,'nome_empresa':nome_empresa,'rua_empresa':rua_empresa,'numero_empresa':numero_empresa,'bairro_empresa':bairro_empresa,
		'cep_empresa':cep_empresa, 'cidade_empresa':cidade_empresa, 'estado_empresa':estado_empresa,
		
		#dados de RAC
		'rac_total_co2':rac_total_co2,'rac_emissoes_equivalentes':rac_emissoes_equivalentes,
		
		#dados de ECM
		'ecm_fossil_co2':ecm_fossil_co2,'ecm_emissoes_equivalentes':ecm_emissoes_equivalentes,'ecm_emissoes_biomassa':ecm_emissoes_biomassa,'ecm_bio_co2':ecm_bio_co2,
		
		#dados de ECE
		'ece_fossil_co2':ece_fossil_co2,'ece_emissoes_equivalentes':ece_emissoes_equivalentes,
		
		#dados de ECV
		'ecv_fossil_co2':ecv_fossil_co2,'ecv_fossil_ch4':ecv_fossil_ch4, 'ecv_fossil_n2o':ecv_fossil_n2o,'ecv_emissoes_equivalentes':ecv_emissoes_equivalentes,'ecv_emissoes_biomassa':ecv_emissoes_biomassa,'ecv_bio_co2':ecv_bio_co2,
		#############################################################################################################################
		#total de CH4 e N2O
		'total_equivalente_ch4':total_equivalente_ch4,'total_equivalente_n2o':total_equivalente_n2o,		
		
		#total de emissoes relativos a CO2
		'total_emissoes_equivalentes_co2':total_emissoes_equivalentes_co2,
		
		#total de emissoes biomassa relativos a CO2
		'total_emissoes_biomassa_co2':total_emissoes_biomassa_co2,
		
		#total geral de emissoes CO2 equivalente
		'total_geral_equivalentes':total_geral_equivalentes,
		
		#total geral de emissoes CO2 biomassa
		'total_geral_biomassa':total_geral_biomassa,'msg2':msg2},context_instance=RequestContext(request))
			

				
def gen_graph_energia(request):
	inventario=Inventario.objects.get()
	empresa=Empresa.objects.get(inventario=inventario)#get da empresa
	nome_empresa=empresa.nome
	rua_empresa=empresa.rua
	numero_empresa=empresa.numero
	bairro_empresa=empresa.bairro
	cep_empresa=empresa.cep
	cidade_empresa=empresa.cidade
	estado_empresa=empresa.estado
	inventario=inventario.ano #ano do
	
	
	totalecv=TotalECV.objects.all() #busca totais de ECM salvos 
	countecv=totalecv.count()	#atualiza o numero do id 
	
	totalece=TotalECE.objects.all() #busca totais de ECE salvos 
	countece=totalece.count()	#atualiza o numero do id
	
	totalecm=TotalECM.objects.all() #busca totais de ECV salvos 
	countecm=totalecm.count()	#atualiza o numero do id
	
	totalced=TotalCED.objects.all() #busca totais de CED salvos 
	countced=totalced.count()	#atualiza o numero do id
	
	totalrac=TotalRAC.objects.all() #busca totais de RAC salvos 
	countrac=totalrac.count()	#atualiza o numero do id 	
	
	
	#############################################################################
	
	 
	if totalced.exists() or totalrac.exists() or totalecm.exists() or totalece.exists() or totalecv.exists():
		#totais de CED
		totalced=TotalCED.objects.get(pk=countced) #pega o objeto mais atual
		ced_fossil_co2=totalced.fossilced_co2
		ced_fossil_ch4=totalced.fossilced_ch4
		ced_fossil_n2o=totalced.fossilced_n2o				
		ced_bioco2=totalced.bioced_co2
		ced_bioch4=totalced.bioced_ch4
		ced_bion2o=totalced.bioced_n2o
		ced_emissoes_equivalentes=totalced.emissoes_equivalentes_ced
		ced_emissoes_biomassa=totalced.emissoes_biomassa_ced
		
			
	############################################################################	
	
		totalrac=TotalRAC.objects.get(pk=countrac)
		rac_total_co2=totalrac.totalrac_co2
		rac_emissoes_equivalentes=totalrac.emissoes_equivalentes_rac
		
	############################################################################	
		
		totalecm=TotalECM.objects.get(pk=countecm)
		ecm_fossil_co2=totalecm.ecm_fossil_co2
		ecm_bio_co2=totalecm.ecm_bio_co2		
		ecm_emissoes_equivalentes=totalecm.ecm_emissoes_equivalentes
		ecm_emissoes_biomassa=totalecm.ecm_emissoes_biomassa
		
	############################################################################
	
		totalece=TotalECE.objects.get(pk=countece)
		ece_fossil_co2=totalece.ece_fossil_co2
		ece_emissoes_equivalentes=totalece.ece_emissoes_equivalentes
		
	############################################################################
	
		totalecv=TotalECV.objects.get(pk=countecv)
		ecv_fossil_co2=totalecv.ecv_fossil_co2
		ecv_fossil_ch4=totalecv.ecv_fossil_ch4
		ecv_fossil_n2o=totalecv.ecv_fossil_n2o
		ecv_bio_co2=totalecv.ecv_bio_co2
		ecv_bio_ch4=totalecv.ecv_bio_ch4
		ecv_bio_n2o=totalecv.ecv_bio_n2o
		ecv_emissoes_equivalentes=totalecv.ecv_emissoes_equivalentes
		ecv_emissoes_biomassa=totalecv.ecv_emissoes_biomassa
	
	############################################################################
	
	
		total_emissoes_equivalentes_co2=ced_fossil_co2+ecm_fossil_co2+ecv_fossil_co2+rac_total_co2+ece_fossil_co2
	
		total_emissoes_biomassa_co2=ecv_bio_co2+ecm_bio_co2+ecv_bio_co2
	
		total_equivalente_ch4=ced_fossil_ch4+ecv_fossil_ch4
		total_equivalente_n2o=ced_fossil_n2o+ecv_fossil_n2o
	
		total_geral_equivalentes=ced_emissoes_equivalentes+ecv_emissoes_equivalentes+ecm_emissoes_equivalentes+ece_emissoes_equivalentes+rac_emissoes_equivalentes
	
		total_geral_biomassa=ecv_emissoes_biomassa+ced_emissoes_biomassa
		totalmes1=totalmes2=totalmes3=totalmes4=totalmes5=totalmes6=totalmes7=totalmes8=totalmes9=totalmes10=totalmes11=totalmes12=0
		emissoesmovel=FonteECE.objects.all()
		if emissoesmovel.exists():
			#count=emissoesmovel.count()
			#return HttpResponse("count =%d" %count)]
			mes1=FonteECE.objects.filter(mes=1)
			mes2=FonteECE.objects.filter(mes=2)
			mes3=FonteECE.objects.filter(mes=3)
			mes4=FonteECE.objects.filter(mes=4)
			mes5=FonteECE.objects.filter(mes=5)
			mes6=FonteECE.objects.filter(mes=6)
			mes7=FonteECE.objects.filter(mes=7)
			mes8=FonteECE.objects.filter(mes=8)
			mes9=FonteECE.objects.filter(mes=9)
			mes10=FonteECE.objects.filter(mes=10)
			mes11=FonteECE.objects.filter(mes=11)
			mes12=FonteECE.objects.filter(mes=12)

			for emissao in mes1:
				totalmes1+=emissao.quantidade
			for emissao in mes2:
				totalmes2+=emissao.quantidade
			for emissao in mes3:
				totalmes3+=emissao.quantidade
			for emissao in mes4:
				totalmes4+=emissao.quantidade
			for emissao in mes5:
				totalmes5+=emissao.quantidade
			for emissao in mes6:
				totalmes6+=emissao.quantidade
			for emissao in mes7:
				totalmes7+=emissao.quantidade
			for emissao in mes8:
				totalmes8+=emissao.quantidade
			for emissao in mes9:
				totalmes9+=emissao.quantidade
			for emissao in mes10:
				totalmes10+=emissao.quantidade
			for emissao in mes11:
				totalmes11+=emissao.quantidade
			for emissao in mes12:
				totalmes12+=emissao.quantidade
			
			heigth = 800
			width = 400		
			data=[totalmes1,totalmes2,totalmes3,totalmes4,totalmes5,totalmes6,totalmes7,totalmes8,totalmes9,totalmes10,totalmes11,totalmes12,]
			v_labels = ["Energia Elétrica","CO2-e(toneladas métricas)"]
			h_labels = ["Janeiro", "Fevereiro", "Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]		   
			pp = CairoPlot.BarPlot("genergia.png", data, heigth, width, background = None, border = 20, grid = True, rounded_corners = True, h_labels=h_labels,v_labels=v_labels) 
			pp.render()
			response = HttpResponse(mimetype="image/png")
			pp.surface.write_to_png(response)
			return response	
	else:
		msg3="sem números relevantes, reveja os cálculos!"
		return render_to_response('resumo/pagina_resumo.html',{'ced_fossil_co2':ced_fossil_co2,'ced_fossil_ch4':ced_fossil_ch4,'ced_fossil_n2o':ced_fossil_n2o,'ced_emissoes_equivalentes':ced_emissoes_equivalentes,
		'ced_emissoes_biomassa':ced_emissoes_biomassa,'ced_bioco2':ced_bioco2,'ced_bioch4':ced_bioch4,'ced_bion2o':ced_bion2o,
		
		#dados da empresa
		'inventario':inventario,'nome_empresa':nome_empresa,'rua_empresa':rua_empresa,'numero_empresa':numero_empresa,'bairro_empresa':bairro_empresa,
		'cep_empresa':cep_empresa, 'cidade_empresa':cidade_empresa, 'estado_empresa':estado_empresa,
		
		#dados de RAC
		'rac_total_co2':rac_total_co2,'rac_emissoes_equivalentes':rac_emissoes_equivalentes,
		
		#dados de ECM
		'ecm_fossil_co2':ecm_fossil_co2,'ecm_emissoes_equivalentes':ecm_emissoes_equivalentes,'ecm_emissoes_biomassa':ecm_emissoes_biomassa,'ecm_bio_co2':ecm_bio_co2,
		
		#dados de ECE
		'ece_fossil_co2':ece_fossil_co2,'ece_emissoes_equivalentes':ece_emissoes_equivalentes,
		
		#dados de ECV
		'ecv_fossil_co2':ecv_fossil_co2,'ecv_fossil_ch4':ecv_fossil_ch4, 'ecv_fossil_n2o':ecv_fossil_n2o,'ecv_emissoes_equivalentes':ecv_emissoes_equivalentes,'ecv_emissoes_biomassa':ecv_emissoes_biomassa,'ecv_bio_co2':ecv_bio_co2,
		#############################################################################################################################
		#total de CH4 e N2O
		'total_equivalente_ch4':total_equivalente_ch4,'total_equivalente_n2o':total_equivalente_n2o,		
		
		#total de emissoes relativos a CO2
		'total_emissoes_equivalentes_co2':total_emissoes_equivalentes_co2,
		
		#total de emissoes biomassa relativos a CO2
		'total_emissoes_biomassa_co2':total_emissoes_biomassa_co2,
		
		#total geral de emissoes CO2 equivalente
		'total_geral_equivalentes':total_geral_equivalentes,
		
		#total geral de emissoes CO2 biomassa
		'total_geral_biomassa':total_geral_biomassa,'msg3':msg3},context_instance=RequestContext(request))	
		
			
			


