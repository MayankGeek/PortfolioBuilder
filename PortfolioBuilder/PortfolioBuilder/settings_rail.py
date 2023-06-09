from PortfolioBuilder.settings import *
from decouple import config
import os 
import cloudinary
SECRET_KEY=config('SECRET_KEY')
ALLOWED_HOSTS = ['portfoliobuilder-production.up.railway.app','127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://portfoliobuilder-production.up.railway.app']
#SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'https://portfoliobuilder-production.up.railway.app/accounts/google/login/callback/'
ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
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

cloudinary.config(
  cloud_name=config('cloud_name'),
  api_key=config('api_key'),
  api_secret=config('api_secret'),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "crispy_forms",
    "crispy_bootstrap5",
    'easy_thumbnails',
    'allauth.socialaccount.providers.google',
    'Home',
    'whitenoise.runserver_nostatic', # new
    'cloudinary',
]