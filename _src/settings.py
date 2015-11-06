import os
import sys

BASE_DIR = os.path.dirname(__file__)

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


INSTALLED_APPS = (
    'djtags',
)

TEMPLATES_ROOT = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

SECRET_KEY = '38b04933-ee7a-48d7-8199-f4acb8c4da0f'
