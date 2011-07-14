from django.conf.urls.defaults import *
from settings import LOCAL,MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
 

    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': '/var/www/massivecoupon/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
                    
     #includes
    (r'^$', include('principal.urls')),
    (r'^noticias/', include('noticias.urls')),
    (r'^conta/', include('contas.urls')),
#    (r'^boleto/', include('boleto.urls')),#inseria midia propria -->url(r'imagem_barras/$', imagem_barras, name='imagem_barras'),
#    (r'^conta/', include('django.contrib.auth.urls')),
)

if LOCAL:
    urlpatterns = urlpatterns + patterns('',
        ((r'^media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': MEDIA_ROOT})),
                                  
        )
#    
handler404 = 'views.file_not_found_404'
handler500 = 'views.server_error_500'