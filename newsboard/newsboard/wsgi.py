"""
WSGI config for newsboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ['DJANGO_ENV'] in ("prod", "production"):
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "newsboard.settings.production"
    )
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsboard.settings.dev")

application = get_wsgi_application()
