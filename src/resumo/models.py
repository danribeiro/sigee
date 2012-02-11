from django.db import models

# Create your models here.

from inventario.models import Inventario
from combustao_movel.models import *
from compra_vapor.models import *
from compra_energia.models import *
from emissao_rac.models import *

class resumo(models.Model):
	inventario=models.OneToOneField(Inventario)
	
	def __unicode__(self):
		return self.inventario
	
