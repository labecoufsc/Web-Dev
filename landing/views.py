from django.http import HttpResponse
from django.template import loader


def boias(request):
    template = loader.get_template('landing/boias.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('landing/about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('landing/contact.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render())

def mapaFlorianopolis(request):
    template = loader.get_template('landing/mapaFlorianopolis.html')
    return HttpResponse(template.render())