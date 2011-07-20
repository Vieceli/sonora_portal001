# Create your views here.
from artistas.forms import ArtistaForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from artistas.models import Artista

def artistas(request,template_name):
    usuario=request.user
    noticias = Artista.objects.all().order_by('-atualizado_em')
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def artista(request,template_name, artista_slug):
    usuario=request.user
    
#    if request.method == 'GET':
#        GET = request.GET  
#        if GET.has_key('a'):  
#            form = ArtistaForm(request.GET'  
    noticia = get_object_or_404(Artista, slug=artista_slug)
    noticias_recentes = Artista.objects.all().order_by('-atualizado_em')
    
    if request.method == 'POST': 
        POST=request.POST
        print POST
        artista_form = ArtistaForm(request.POST)
        if artista_form.is_valid(): 
            artista_form.save()
            return HttpResponseRedirect('/Obrigado/')
       
    else:
        artista_form = ArtistaForm()
        
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

