import os
import sys
from django.core.wsgi import get_wsgi_application


os.environ['DJANGO_SETTINGS_MODULE'] = 'talk_with_unknown.settings'


application = get_wsgi_application()
app = application