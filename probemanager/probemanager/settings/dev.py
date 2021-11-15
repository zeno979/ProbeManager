from probemanager.settings.base import *  # noqa
from core.git import git_tag
import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.join(ROOT_DIR, 'conf.ini'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'j-93#)n%t8d0%tyo$f2e+$!%5-#wj65d#85@9y8jf)%_69_1ek'
FERNET_KEY = b'ly8WTzGyN6Xz23t5yq_s_1Ob-qmccqdi52Baj4ta_qQ='

GIT_BINARY = config['GIT']['GIT_BINARY']

VERSION = git_tag(ROOT_DIR)

# Celery settings
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

TIME_ZONE = 'UTC'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/probemanager.sqlite'
    }
}

SPECIFIC_APPS = ['suricata', 'checkcve', 'bro']
INSTALLED_APPS = BASE_APPS + SPECIFIC_APPS

for app in SPECIFIC_APPS:
    LOGGING['loggers'].update({app: {'handlers': ['console'], 'propagate': True}})
    if os.path.isfile(BASE_DIR + "/" + app + "/settings.py"):
        exec(open(BASE_DIR + "/" + app + "/settings.py").read())

LOGGING['handlers']['file'].update({'filename': os.path.join(BASE_DIR, 'probemanager.log')})
LOGGING['handlers']['file-error'].update({'filename': os.path.join(BASE_DIR, 'probemanager-error.log')})

TEMPLATES[0]['OPTIONS']['debug'] = True
