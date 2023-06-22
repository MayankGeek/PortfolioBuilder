from PortfolioBuilder.settings import *
from decouple import config
import os 

SECRET_KEY=config('SECRET_KEY')
ALLOWED_HOSTS = ['portfoliobuilder-production.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://portfoliobuilder-production.up.railway.app']
#SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'https://portfoliobuilder-production.up.railway.app/accounts/google/login/callback/'
DEBUG = False
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # new

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST'),
            'PORT': config('DATABASE_PORT'),
            'OPTIONS': {'sslmode': 'require'},
        }
}
 
