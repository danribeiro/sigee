from django.conf.urls.defaults	import  patterns, url
from fonte_emissao import views

urlpatterns = patterns('fonte_emissao.views',
    #urls do modelo de fontes de emissao
    url(r'^lista_fonte/$','lista_fonte', name='lista_fonte'),
    url(r'^adiciona_fonte/$','adiciona_fonte', name='adiciona_fonte'),
   # url(r'^item_fonte/(?P<nr_item>\d+)/$','item',name='item'),    
    url(r'^remove_fonte/(?P<nr_item>\d+)/$','remove_fonte',name='remove_fonte'),
    url(r'^edita_fonte/(?P<nr_item>\d+)/$','edita_fonte',name='edita_fonte'),
    url(r'^gerapdf_fonte/$','gerapdf_fonte',name='gerapdf_fonte'),
    
     
    #urls do modelo de fatores ch4 e n2o/setor de atividade 
    url(r'^adiciona_ef/$','adiciona_ef',name='adiciona_ef'),
    url(r'^remove_ef/(?P<nr_item>\d+)/$','remove_setor',name='remove_setor'),
    url(r'^lista_ef/$','lista_ef',name='lista_ef'),
    url(r'^edita_ef/(?P<nr_item>\d+)/$','edita_ef', name='edita_ef'),
    
    #urls do modelo de setores de atividade
    url(r'^adiciona_setor/$','adiciona_setor',name='adiciona_setor'),
    url(r'^lista_setor/$','lista_setor', name='lista_setor'),
    url(r'^remove_setor/(?P<nr_item>\d+)/$','remove_setor', name='remove_setor'),
    url(r'^edita_setor/(?P<nr_item>\d+)/$','edita_setor', name='edita_setor'),
    
    
)
