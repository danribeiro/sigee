from django.contrib import admin
from inventario.models import Empresa, Inventario, CED, FonteCED
admin.site.register(Empresa)
admin.site.register(Inventario)
admin.site.register(CED)
admin.site.register(FonteCED)

class EmpresaAdmin(admin.ModelAdmin):
	fields=('nome','rua','numero','bairro','complemento','cep','cidade','estado')
	list_display=('nome','rua','numero','bairro','cidade','cep','estado')


class InventarioAdmin(admin.ModelAdmin):
	fields=('empresa','data','ano')
	list_display=('empresa','data','ano')


class CEDAdmin(admin.ModelAdmin):
	fields=('inventario','setor_atividade','fontes_emissao')
	list_display=('inventario','setor_atividade','fontes_emissao')
	
