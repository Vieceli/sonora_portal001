# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from sonora_portal001.noticias.models import Noticia
from django.template.context import RequestContext

def noticias(request,template_name):
    usuario=request.user
    noticias = Noticia.objects.all().order_by('-atualizado_em')
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def noticia(request,template_name,noticia_slug):
    noticia = get_object_or_404(Noticia, slug=noticia_slug)
    noticias_recentes = Noticia.objects.all().order_by('-atualizado_em')
    usuario=request.user
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))