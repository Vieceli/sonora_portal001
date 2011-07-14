# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from sonora_portal001.principal.forms import FormCadEmail
from sonora_portal001.principal.models import Cadastra_Email, Link
from sonora_portal001.noticias.models import Noticia

def index(request):
    usuario=request.user
    noticias = Noticia.objects.all().order_by('-atualizado_em')[:5]
    links = Link.objects.all().order_by('-atualizado_em')[:5]

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

