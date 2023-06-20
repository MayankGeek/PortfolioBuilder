from PortfolioBuilder.settings import *
from decouple import config
SECRET_KEY=config('SECRET_KEY')
ALLOWED_HOSTS = ['portfoliobuilder-production.up.railway.app']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"