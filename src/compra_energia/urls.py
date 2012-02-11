#-*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('compra_energia.views',
    #urls do modelo de emissão por compra de energia 
    url(r'^lista_ece/$','lista_ece', name='lista_ece'),
    url(r'^adiciona_ece/$','adiciona_ece', name='adiciona_ece'), 
    url(r'^remove_ece/(?P<nr_item>\d+)/$','remove_ece',name='remove_ece'),
    url(r'^calcula_ece/(?P<nr_item>\d+)/$','calcula_ece',name='calcula_ece'),
    url(r'^edita_ece/(?P<nr_item>\d+)/$','edita_ece',name='edita_ece'),   
    
    #urls do modelo de fonteECE
   
    url(r'^adiciona_fonteece/$','adiciona_fonteece',name='adiciona_fonteece'),
    url(r'^lista_fonteece/$','lista_fonteece', name='lista_fonteece'),
    url(r'^remove_fonteece/(?P<nr_item>\d+)/$','remove_fonteece', name='remove_fonteece'),
    url(r'^edita_fonteece/(?P<nr_item>\d+)/$','edita_fonteece', name='edita_fonteece'),
    
    #url(r'^hellopdf/$','hellopdf', name='hellopdf'),
    
    
   )
