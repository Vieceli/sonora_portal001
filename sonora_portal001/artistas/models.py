# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Artista(models.Model):
    class Meta:
        db_table = 'artistas'
        verbose_name = _('Artista')
        verbose_name_plural = _('Artistas')
        
    nome                = models.CharField("Nome",max_length=255,
                              help_text=u'Nome do Artista',default='Lorem Ipsum')
    subtitulo           = models.CharField("Subtitulo",max_length=255,
                              help_text=u'Subtitulo da noticia',default='Lorem ipsum dolor sit amet!')
    resumo              = models.TextField(u"Descrição",max_length=30,
                              help_text=u'Digite 30 caracteres resumindo o Artista' )
    url                 = models.URLField(u"Endereço na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com')
    slug                = models.SlugField(unique=True)
    imagem              = models.ImageField(upload_to='img_artista/', blank=False)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome
    
    #def get_absolute_url(self):
    #     return reverse('noticias', kwargs={'noticia_slug': self.pk})
    def get_absolute_url(self):
        return reverse('artista', kwargs={'artista_slug': self.slug})
#    def get_absolute_url(self):

class Artista_Contato(models.Model):
    class Meta:
        db_table = 'artista_contato'
        verbose_name = _('Artista_em_contato')
        verbose_name_plural = _('Artistas_em_contato')
        
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
    telefone        = models.CharField(u"Telefone",max_length=400,
                              help_text=u'Telefone',default='123456789')
    arquivo         = models.FileField(upload_to='artista_arquivo', max_length=20)
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