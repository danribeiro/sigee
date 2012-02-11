#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('combustao_movel.views',
    #urls do modelo de emissão por combustão 
    url(r'^lista_ecm/$','lista_ecm', name='lista_ecm'),
    url(r'^adiciona_ecm/$','adiciona_ecm', name='adiciona_ecm'), 
    url(r'^remove_ecm/(?P<nr_item>\d+)/$','remove_ecm',name='remove_ecm'),
    url(r'^calcula_ecm/(?P<nr_item>\d+)/$','calcula_ecm',name='calcula_ecm'),
    url(r'^edita_ecm/(?P<nr_item>\d+)/$','edita_ecm',name='edita_ecm'),      
    
    #urls do modelo de fonteECM
    url(r'^adiciona_fonteecm/$','adiciona_fonteecm',name='adiciona_fonteecm'),
    url(r'^lista_fonteecm/$','lista_fonteecm', name='lista_fonteecm'),
    url(r'^remove_fonteecm/(?P<nr_item>\d+)/$','remove_fonteecm', name='remove_fonteecm'),
    url(r'^edita_fonteecm/(?P<nr_item>\d+)/$','edita_fonteecm',name='edita_fonteecm'),   
    
    
    #urls do modelo Fatores Variáveis
    url(r'^adiciona_fator/$','adiciona_fator',name='adiciona_fator'),
    url(r'^lista_fator/$','lista_fator', name='lista_fator'),
    url(r'^remove_fator/(?P<nr_item>\d+)/$','remove_fator', name='remove_fator'),
    url(r'^edita_fator/(?P<nr_item>\d+)/$','edita_fator', name='edita_fator'),
   
    
    #urls do modelo Parâmetros
    url(r'^adiciona_param/$','adiciona_param',name='adiciona_param'),
    url(r'^lista_param/$','lista_param', name='lista_param'),
    url(r'^remove_param/(?P<nr_item>\d+)/$','remove_param', name='remove_param'),
    url(r'^edita_param/(?P<nr_item>\d+)/$','edita_param', name='edita_param'),
    
    
    #urls do modelo FonteEmissaoECM
    url(r'^adiciona_emissaoecm/$','adiciona_emissaoecm',name='adiciona_emissaoecm'),
    url(r'^lista_emissaoecm/$','lista_emissaoecm', name='lista_emissaoecm'),
    url(r'^remove_emissaoecm/(?P<nr_item>\d+)/$','remove_emissaoecm', name='remove_emissaoecm'),
    url(r'^edita_emissaoecm/(?P<nr_item>\d+)/$','edita_emissaoecm', name='edita_emissaoecm'),
    
    
    
)
