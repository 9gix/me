# -*- coding: utf-8 -*-
# Local settings for me project.

LOCAL_SETTINGS = True
from settings import *

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

#sorl-thumbnail
THUMBNAIL_DEBUG = True

#django-contact-form
DEFAULT_FROM_EMAIL = 'me@localhost'

MANAGERS = (
    ('me','me@localhost'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                             # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ABC'
EMAIL_HOST_PASSWORD = 'ABC'
EMAIL_USE_TLS = True

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHE_BACKEND = 'locmem:///'
CACHE_MIDDLEWARE_SECONDS = 60*5
CACHE_MIDDLEWARE_KEY_PREFIX = 'mingus.'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

INTERNAL_IPS = ('127.0.0.1',)

### DEBUG-TOOLBAR SETTINGS
DEBUG_TOOLBAR_CONFIG = {
'INTERCEPT_REDIRECTS': False,
}

#django-degug-toolbar
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

### django-markup
MARKUP_CHOICES = (
	'none',	
	'markdown',
	'textile',
	'restructuredtext',
)

#django-request
REQUEST_IGNORE_PATHS = (
        r'^admin/(.*)',
        r'^media/(.*)',
        r'^favicon\.ico|favicon\.ico/$',
        r'^__debug__/',
		r'^tinymce/(.*)',
)

