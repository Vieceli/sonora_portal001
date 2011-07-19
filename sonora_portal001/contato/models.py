# -*- coding: utf-8 -*- 
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from campo_personalizado import TelefoneField
from contato.campo_personalizado import ContentTypeRestrictedFileField

#OFERTA_IMG = 'cupon_imagens/'
#OFERTA_MINI = 'cupon_mini/'

class Parceiro(models.Model):
    class Meta:
        db_table = 'parceiros'
        verbose_name = _('Parceiro')
        verbose_name_plural = _('Parceiros')
        
    nome            = models.CharField("Nome do Parceiro",max_length=40,
                              help_text=u'nome do Parceiro',default='Lorem Ipsum')
    empresa         = models.CharField("Nome da Empresa",max_length=40,
                              help_text=u'Nome da Empresa',default='Lorem Ipsum',blank=True,)
    site            = models.URLField(u"Seu site na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    email           = models.EmailField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    telefone        = TelefoneField()
    mensagem     = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome

class Radialista(models.Model):
    class Meta:
        db_table = 'radialistas'
        verbose_name = _('Radialista')
        verbose_name_plural = _('Radialistas')
        
    nome_radio      = models.CharField("Nome da Radio",max_length=40,
                              help_text=u'nome da Radio',default='Lorem Ipsum')
    frequencia      = models.CharField(u"Frequência da Radio",max_length=40,
                              help_text=u'Frequência da Radio',default='Lorem Ipsum')
    slogan          = models.CharField(u"Slogan da Radio",max_length=40,
                              help_text=u'Slogan da Radio',default='Lorem Ipsum')
    programador     = models.CharField(u"Programador da Radio",max_length=40,
                              help_text=u'Programador da Radio',default='Lorem Ipsum')
    direcao         = models.CharField(u"Direção da Radio",max_length=40,
                              help_text=u'Direção da Radio',default='Lorem Ipsum')
    email           = models.EmailField()
    telefone        = TelefoneField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    mensagem        = models.TextField()
    anexo           = ContentTypeRestrictedFileField(
                                                     #upload_to='radialista_anexo',
                                                     content_types=['application/mp3', 'application/pdf', 'application/odt', 
                                                                    'application/docx','application/jpg','application/png',
                                                                    'application/gif','application/txt', 
                                                                    'application/zip','application/tar'],
                                                     max_upload_size=20971520)
    site            = models.URLField(u"Site da radio",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    facebook        = models.CharField(u"Facebook",max_length=400,
                              help_text=u'Facebook',default='Lorem Ipsum')
    twitter         = models.CharField(u"Twitter",max_length=400,
                              help_text=u'Twitter',default='Lorem Ipsum')
    youtube         = models.CharField(u"YouTube",max_length=400,
                              help_text=u'YouTube',default='Lorem Ipsum')

    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome_radio
    
class Compositor(models.Model):
    class Meta:
        db_table = 'compositores'
        verbose_name = _('Compositor')
        verbose_name_plural = _('Compositores')
        
    nome            = models.CharField("Nome do Compositor",max_length=40,
                              help_text=u'nome do Compositor',default='Lorem Ipsum')
    arquivo         = ContentTypeRestrictedFileField(
                                                     #upload_to='compositor_arquivo',
                                                     content_types=['application/pdf', 'application/odt', 
                                                                    'application/docx','application/txt'],
                                                     max_upload_size=20971520)
    midia           = ContentTypeRestrictedFileField(
                                                     #upload_to='compositor_midia',
                                                     content_types=['application/mp3', 'application/jpg', 
                                                                    'application/png','application/gif'],
                                                     max_upload_size=20971520)
    email           = models.EmailField()
    telefone        = TelefoneField()
    mensagem        = models.TextField()
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome
    
class Contratante(models.Model):
    class Meta:
        db_table = 'contratantes'
        verbose_name = _('Contratante')
        verbose_name_plural = _('Contratantes')
        
    nome            = models.CharField("Nome do Contratante",max_length=40,
                              help_text=u'Nome do Contratante',default='Lorem Ipsum')
    empresa         = models.CharField("Empresa do Contratante",max_length=40,
                              help_text=u'Empresa do Contratante',default='Lorem Ipsum',blank=True,)
    site            = models.URLField(u"Seu site na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    email           = models.EmailField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    telefone        = TelefoneField()
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome

class Artista_Contato(models.Model):
    class Meta:
        db_table = 'artista'
        verbose_name = _('Artista')
        verbose_name_plural = _('Artistas')
        
    nome            = models.CharField("Nome do Artista",max_length=40,
                              help_text=u'Nome do Artista',default='Lorem Ipsum')
    site            = models.URLField(u"Seu site na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    email           = models.EmailField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    telefone        = TelefoneField()
    anexo         = ContentTypeRestrictedFileField(
                                                   #upload_to='artista_arquivo',
                                                     content_types=['application/pdf', 'application/odt', 
                                                                    'application/docx','application/txt',
                                                                    'application/pdf', 'application/odt', 
                                                                    'application/docx','application/txt'],
                                                     max_upload_size=20971520)
    facebook        = models.CharField(u"Facebook",max_length=400,
                              help_text=u'Facebook',default='Lorem Ipsum')
    twitter         = models.CharField(u"Twitter",max_length=400,
                              help_text=u'Twitter',default='Lorem Ipsum')
    youtube         = models.CharField(u"YouTube",max_length=400,
                              help_text=u'YouTube',default='Lorem Ipsum')
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome

class Contato(models.Model):
    class Meta:
        db_table = 'contato'
        verbose_name = _('Contato')
        verbose_name_plural = _('Contatos')
        
    nome            = models.CharField("Nome",max_length=40,
                              help_text=u'Nome',default='Lorem Ipsum')
    email           = models.EmailField()
    telefone        = TelefoneField()
    anexo           = ContentTypeRestrictedFileField(
                                                   #upload_to='contato_arquivo',
                                                     content_types=['application/pdf', 'application/odt', 
                                                                    'application/docx','application/txt',
                                                                    'application/pdf', 'application/odt', 
                                                                    'application/docx','application/txt'],
                                                     max_upload_size=20971520)
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome
    
