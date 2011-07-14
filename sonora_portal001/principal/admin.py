# -*- coding: utf-8 -*-
from django.contrib import admin

from sonora_portal001.principal.models import Cadastra_Email, Link
from sonora_portal001.principal.forms import NoticiaAdminForm
from sonora_portal001.noticias.models import Noticia

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

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

    
admin.site.register(Cadastra_Email, Cadastra_Email_Admin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Link, LinkAdmin)
