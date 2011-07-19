# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from contato.forms import ContatoForm, ContratantesForm, CompositoresForm,RadialistaForm, ArtistaForm, ParceiroForm


def contato(request,template_name):
    usuario=request.user
    
#    if request.method == 'GET':
#        GET = request.GET  
#        if GET.has_key('a'):  
#            form = ArtistaForm(request.GET'  
#    
    if request.method == 'POST': 
        POST=request.POST
        print POST
        if POST.has_key('contato'):
            contato_form = ContatoForm(request.POST)
            if contato_form.is_valid(): 
                contato_form.save()
                return HttpResponseRedirect('/Obrigado/')
        elif POST.has_key('contratante'):
            contratante_form = ContratantesForm(request.POST)
            if contratante_form.is_valid(): 
                contratante_form.save()
                return HttpResponseRedirect('/Obrigado/')
        elif POST.has_key('compositor'):
            compositor_form = CompositoresForm(request.POST)
            if compositor_form.is_valid(): 
                compositor_form.save()
                return HttpResponseRedirect('/Obrigado/')
        elif POST.has_key('radialista'):
            radialista_form = RadialistaForm(request.POST)
            if radialista_form.is_valid(): 
                radialista_form.save()
                return HttpResponseRedirect('/Obrigado/')
        elif POST.has_key('artista'):
            artista_form = ArtistaForm(request.POST)
            if artista_form.is_valid(): 
                artista_form.save()
                return HttpResponseRedirect('/Obrigado/')
        elif POST.has_key('parceiro'):
            parceiro_form = ParceiroForm(request.POST)
            if parceiro_form.is_valid(): 
                parceiro_form.save()
                return HttpResponseRedirect('/Obrigado/')  
       
    else:
        contato_form = ContatoForm()
        contratante_form = ContratantesForm() 
        compositor_form = CompositoresForm()
        artista_form = ArtistaForm()
        radialista_form = RadialistaForm()
        parceiro_form = ParceiroForm() 

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

