"""
<<<<<<<< HEAD:django_blog/django_blog/wsgi.py
WSGI config for django_blog project.
========
WSGI config for advanced_api_project project.
>>>>>>>> 01a850dae2c214b543d28b8224f3639fdfa888ed:advanced_api_project/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<<< HEAD:django_blog/django_blog/wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
>>>>>>>> 01a850dae2c214b543d28b8224f3639fdfa888ed:advanced_api_project/wsgi.py

application = get_wsgi_application()
