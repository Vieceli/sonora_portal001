# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

from principal.models import Cadastra_Email, Link
from noticias.models import Noticia
from artistas.models import Artista, Artista_Contato
from parceiros.models import Parceiro, Contratante, Compositor, Radialista
from contato.models import Contato
from noticias.forms import NoticiaAdminForm


class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/textareas.js')

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    form = NoticiaAdminForm
    date_hierarchy = 'criado_em'
    prepopulated_fields = {'slug':('titulo',)}
    list_display = ['titulo', 'atualizado_em', 'miniatura']
    list_filter = ('titulo', 'atualizado_em')
    list_per_page = 10
    search_fields = ['titulo',]
    
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/textareas.js')
    
class Cadastra_Email_Admin(admin.ModelAdmin):
    """ka"""
    list_display = ['email','remover']

class LinkAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    prepopulated_fields = {'slug':('titulo',)}
    list_display = ['titulo', 'atualizado_em', 'miniatura']
    list_filter = ('titulo', 'atualizado_em')
    list_per_page = 10
    search_fields = ['titulo',]


class ArtistaAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    prepopulated_fields = {'slug':('nome',)}
    list_display = ['nome', 'atualizado_em',]
    list_filter = ('nome', 'atualizado_em')
    list_per_page = 10
    search_fields = ['nome',]

    
admin.site.register(Cadastra_Email, Cadastra_Email_Admin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Artista_Contato)
admin.site.register(Parceiro)
admin.site.register(Contratante)
admin.site.register(Compositor)
admin.site.register(Radialista)
admin.site.register(Contato)

