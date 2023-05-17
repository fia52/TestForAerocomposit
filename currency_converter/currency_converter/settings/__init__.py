"""
This is a django-split-settings main file.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
import os

from dotenv import load_dotenv
from split_settings.tools import optional, include

load_dotenv()

_env = os.getenv('DJANGO_ENV') or 'production'

base_settings = [
    'components/common.py',  # standard django settings
    'components/database.py',

    f'environments/{_env}.py',

    optional('environments/local.py'),
]

include(*base_settings)
