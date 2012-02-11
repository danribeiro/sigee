#-*- coding: utf-8 -*-

from models import resumo
from django  import  forms
from django.forms.models import ModelForm

class FormResumo(forms.ModelForm):
	class Meta:
		model=resumo
