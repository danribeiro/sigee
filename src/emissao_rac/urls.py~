#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('emissao_rac.views',
    #urls do modelo de emissão por R&AC 
    url(r'^lista_rac/$','lista_rac', name='lista_rac'),
    url(r'^adiciona_rac/$','adiciona_rac', name='adiciona_rac'), 
    url(r'^remove_rac/(?P<nr_item>\d+)/$','remove_rac',name='remove_rac'),
    url(r'^calcula_rac/(?P<nr_item>\d+)/$','calcula_rac',name='calcula_rac'),
    url(r'^edita_rac/(?P<nr_item>\d+)/$','edita_rac',name='edita_rac'),   
    
    #urls do modelo de fonteRAC
    url(r'^adiciona_fonterac/$','adiciona_fonterac',name='adiciona_fonterac'),
    url(r'^lista_fonterac/$','lista_fonterac', name='lista_fonterac'),
    url(r'^remove_fonterac/(?P<nr_item>\d+)/$','remove_fonterac', name='remove_fonterac'),
    url(r'^edita_fonterac/(?P<nr_item>\d+)/$','edita_fonterac', name='edita_fonterac'),
    
    #urls do modelo de gas
    url(r'^adiciona_gas/$','adiciona_gas',name='adiciona_gas'),
    url(r'^lista_gas/$','lista_gas', name='lista_gas'),
    url(r'^remove_gas/(?P<nr_item>\d+)/$','remove_gas', name='remove_gas'),
    url(r'^edita_gas/(?P<nr_item>\d+)/$','edita_gas', name='Edita_gas'),
    
    #urls do modelo de parametros    
    url(r'^adiciona_equip/$','adiciona_equip',name='adiciona_equip'),
    url(r'^lista_equip/$','lista_equip', name='lista_equip'),
    url(r'^remove_equip/(?P<nr_item>\d+)/$','remove_equip', name='remove_equip'),
    url(r'^edita_equip/(?P<nr_item>\d+)/$','edita_equip', name='edita_equip'),
    
       
   )
