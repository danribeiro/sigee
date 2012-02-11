#-*- coding: utf-8 -*-

from models import ECE, FonteECE
from django  import  forms
from django.forms.models import ModelForm

class FormECE(forms.ModelForm):
	class Meta:
		model=ECE
		fields=('inventario',)

class FormFonteECE(forms.ModelForm):
	registro_fonte=forms.CharField(max_length=50,required=False)
	descricao_fonte=forms.CharField(max_length=75,required=False)
	class Meta:
		model=FonteECE
		fields=('ece','mes','quantidade','registro_fonte','descricao_fonte')
		
	
