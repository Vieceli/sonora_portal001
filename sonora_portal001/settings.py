# Django settings for apostwithyou001 project.
# -*- coding: utf-8 -*-
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

#redirects
#DEFAULT_CITY_SLUG = 'aposta/pais'
LOGIN_URL = '/contas/login/'
LOGOUT_URL = '/contas/sair/'
LOGIN_REDIRECT_URL = "/"
AUTH_PROFILE_MODULE = 'contas.UserProfile'
#CUSTOM_USER_MODEL = 'contas.MeuUser'
#extra configuracoes
ENABLE_SSL = False
FORCE_SCRIPT_NAME = ''

ADMINS = (
  ('Jhoni', 'veiodruida@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_PATH, 'mycms.db'),
    }
}


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"


TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

try:
    from local_settings import DEBUG,LOCAL,TEMPLATE_DEBUG
    from email_settings import EMAIL_HOST,EMAIL_HOST_PASSWORD,EMAIL_HOST_USER,EMAIL_PORT,EMAIL_USE_TLS
    from site_metas import META_DESCRIPTION,META_KEYWORDS,SESSION_COOKIE_AGE,SITE_NAME
except ImportError:
    pass

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'estatico')
STATIC_URL = '/estatico/'

DJBOLETO_MEDIA_URL = "/media/boletosimg/"

GEOIP_PATH = os.path.join(PROJECT_ROOT_PATH, 'geoip')

ADMIN_MEDIA_PREFIX = '/admin-media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
   # 'apostwithyou001.utils.context_processors',
)
                     
                 

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
                 os.path.join(PROJECT_ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'principal',
    'contas',
    'noticias',
)

AUTHENTICATION_BACKENDS = (
    # this is the default backend, don't forget to include it!
    'backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    # this is what you're adding for using Twitter
#    'socialregistration.auth.TwitterAuth',
#    'socialregistration.auth.FacebookAuth', # Facebook
#    'socialregistration.auth.OpenIDAuth', # OpenID
)
