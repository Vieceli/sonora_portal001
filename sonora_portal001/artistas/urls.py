'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('artistas.views',
          
        url(r'^$', 'artistas', 
            {'template_name':'artistas/artistas.html'}, name='artistas'),
                  
        url(r'^(?P<artista_slug>[-\w]+)/$', 'artista', 
            {'template_name':'artista/artista.html'}, name='artista'),
        )