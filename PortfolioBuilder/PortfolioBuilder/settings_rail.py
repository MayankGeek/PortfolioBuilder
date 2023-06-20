from PortfolioBuilder.settings import *
from decouple import config
SECRET_KEY=config('SECRET_KEY')
ALLOWED_HOSTS = ['portfoliobuilder-production.up.railway.app']
