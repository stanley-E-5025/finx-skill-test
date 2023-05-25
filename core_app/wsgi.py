import os
from django.core.wsgi import get_wsgi_application
from django.core import management

management.call_command("create_users")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_app.settings")
application = get_wsgi_application()
