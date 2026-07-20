import os
import sys

# Add the directory to python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model2.settings")

application = get_wsgi_application()
app = application
