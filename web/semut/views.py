from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 
def mk(request):
    template = loader.get_template('mk.html')
    return HttpResponse(template.render())
def mr(request):
     template = loader.get_template('mr.html')
     return HttpResponse(template.render())
