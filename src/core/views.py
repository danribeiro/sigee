# Create your views here.
#-*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response


def homepage(request):
	return render_to_response('index.html', RequestContext(request))
