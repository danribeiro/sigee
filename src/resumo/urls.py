#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('resumo.views',
    #urls do modelo de emissão por compra de vapor
    url(r'^calcula_resumo/$','calcula_resumo',name='calcula_resumo'),
    url(r'^relatorio_resumo/$','relatorio_resumo',name='relatorio_resumo'),
    url(r'^gen_graph/$','gen_graph',name='gen_graph'),
    url(r'^gen_graph_bio/$','gen_graph_bio',name='gen_graph_bio'),
    url(r'^gen_graph_movel/$','gen_graph_movel',name='gen_graph_movel'),
    url(r'^gen_graph_energia/$','gen_graph_energia',name='gen_graph_energia'),     
   )
