import os


ROOT = os.path.dirname(__file__)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT, "templates"),
)

SECRET_KEY = '38b04933-ee7a-48d7-8199-f4acb8c4da0f'
