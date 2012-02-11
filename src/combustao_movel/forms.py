#-*- coding:  utf-8 -*-

from django.forms.models import ModelForm
from django import forms
from inventario.models import *
from fonte_emissao.models import *
from combustao_movel.models import ECM, FonteECM, FatoresVariaveis, Parametros,FonteEmissaoECM
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError



class FormECM(forms.ModelForm):
	class Meta:
		model=ECM
		exclude=('fontes_emissao',)

class FormFonteECM(forms.ModelForm):
	registro_fonte=forms.CharField(max_length=50,required=False)
	descricao_fonte=forms.CharField(max_length=75,required=False)

	class Meta:
		model=FonteECM
		fields=('ecm','mes','fonte_emissao','quantidade','registro_fonte','descricao_fonte')	
	
class FormFatores(forms.ModelForm):
	class Meta:
		model=FatoresVariaveis
		fields=('ano_param',)
				
class FormParametros(forms.ModelForm):
	class Meta:
		model=Parametros
		fields=('mes','fatores_variaveis','fesin','etanol_gasolina','biodiesel_diesel')

class FormFonteEmissaoECM(forms.ModelForm):
	class Meta:
		model=FonteEmissaoECM
			

		
