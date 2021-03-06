#-*- coding:utf-8 -*- 

from django import forms
from fonte_emissao.models import FonteEmissao,EfSetor, SetorAtividade
from django.utils.safestring import SafeUnicode
from django.forms.models import BaseInlineFormSet, inlineformset_factory

class FonteForm(forms.ModelForm):
    u'''Formulário para fontes de emissão'''
    class Meta:
        model=FonteEmissao

class SetorForm(forms.ModelForm):
	u'''Formulário para adicionar setor de atividade em relação a uma fonte de emissão'''
	class Meta:
		model=SetorAtividade
		exclude=('fonte_emissao',)


class EfSetorForm(forms.ModelForm):
    u'''Formulário para adicionar coeficientes de emissão em relação a um setor de atividade'''
    class Meta:
        model=EfSetor
        
       



