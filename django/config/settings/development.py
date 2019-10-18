from config.settings.common import *


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sub-tracker',
        'USER': 'sub-tracker',
        'PASSWORD': 'development',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
