#urls referentes a views empresa

from django.conf.urls.defaults	import  patterns, url
from inventario import views

urlpatterns=patterns('inventario.views',
	#urls que mapeia as views da empresa
	url(r'^lista_empresa/$', 'lista_empresa',name='lista_empresa'),
	url(r'^adiciona_empresa/$','adiciona_empresa',name ='adiciona_empresa'),
	url(r'^remove_empresa/(?P<nr_item>\d+)/$','remove_empresa',name='remove_empresa'),	
	url(r'^edita_empresa/(?P<nr_item>\d+)/$','edita_empresa',name='edita_empresa'),
	
	
	url(r'^lista_inventario/$','lista_inventario',name='lista_inventario'),
	url(r'^inicia_inventario/$','inicia_inventario', name='inicia_inventario'),
	url(r'^remove_inventario/(?P<nr_item>\d+)/$','remove_inventario',name='remove_inventario'),
	url(r'^edita_inventario/(?P<nr_item>\d+)/$','edita_inventario',name='edita_inventario'),
	
	url(r'^adiciona_ced/$', 'adiciona_ced', name='adiciona_ced'),
	url(r'^calcula_ced/(?P<nr_item>\d+)/$','calcula_ced',name='calcula_ced'),
	url(r'^lista_ced/$','lista_ced',name='lista_ced'),
	url(r'^resumo_ced/$', 'resumo_ced', name='resumo_ced'),
	url(r'^edita_ced/(?P<nr_item>\d+)/$','edita_ced',name='edita_ced'),
	url(r'^remove_ced/(?P<nr_item>\d+)/$','remove_ced',name='remove_ced'),
	url(r'^salva_totalced/$', 'salva_totalced',name='salva_totalced'),
	
	url(r'^adiciona_fonteCED/$', 'adiciona_fonteCED', name='adiciona_fonteCED'),
	url(r'^remove_fonteCED/(?P<nr_item>\d+)/$', 'remove_fonteCED', name='remove_fonteCED'),
	url(r'^lista_fonteCED/$', 'lista_fonteCED', name='lista_fonteCED'),
	url(r'^edita_fonteCED/(?P<nr_item>\d+)/$','edita_fonteCED',name='edita_fonteCED'),
	


)
