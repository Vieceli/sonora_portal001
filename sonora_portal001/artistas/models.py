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
        return reverse('artistas', kwargs={'artista_slug': self.slug})
#    def get_absolute_url(self):