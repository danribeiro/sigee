from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import  staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^src/', include('src.foo.urls')),
    url(r'^$', 'core.views.homepage'),
    url(r'^fonte_emissao/', include('fonte_emissao.urls',namespace='fonte_emissao')),
    url(r'^inventario/',include('inventario.urls',namespace='inventario')),
    url(r'^combustao_movel/',include('combustao_movel.urls',namespace='combustao_movel')),
    url(r'^compra_energia/',include('compra_energia.urls',namespace='compra_energia')),
    url(r'^emissao_rac/',include('emissao_rac.urls',namespace='emissao_rac')),
    url(r'^compra_vapor/',include('compra_vapor.urls',namespace='compra_vapor')),
    url(r'^resumo/',include('resumo.urls',namespace='resumo')),
   # url(r'^info/$,'),
    #url(r'^empresa$,')
    #url(r'^jqdjangogrid/', include('jqdjangogrid.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns+=staticfiles_urlpatterns()
