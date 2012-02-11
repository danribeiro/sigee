#-*- coding:utf-8 -*-
from  django.utils.translation import  ugettext as _
from  django.core.exceptions import  ValidationError

def CePValidator(value):
	if not value.isdigit():
		raise ValidationError(_(u'O CEP deve conter apenas números'))
	if len(value)!=8:
		raise ValidationError(_(u'O CEP deve ter 8 dígitos '))

 
