import os
import sys

path = '/home/alialmandoz/ArchivoImprimirWebApp' # use your own PythonAnywhere username here
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ArchivoImprimir.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())