from PortfolioBuilder.settings import *
from decouple import config
import os 

SECRET_KEY=config('SECRET_KEY')
ALLOWED_HOSTS = ['portfoliobuilder-production.up.railway.app']
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # new