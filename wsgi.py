import os

PROJECT_ROOT = '/'.join([os.path.dirname(os.path.abspath(__file__)), 'developer_box'])
#settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
settings_module= "developer_box.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
