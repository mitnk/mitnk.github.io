import os
import sys

ROOT = os.path.dirname(__file__)

if ROOT not in sys.path:
    sys.path.append(ROOT)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT, "templates"),
)

INSTALLED_APPS = (
    'djtags',
)

SECRET_KEY = '38b04933-ee7a-48d7-8199-f4acb8c4da0f'
