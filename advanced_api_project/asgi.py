"""
<<<<<<<< HEAD:django_blog/asgi.py
ASGI config for django_blog project.
========
ASGI config for advanced_api_project project.
>>>>>>>> 01a850dae2c214b543d28b8224f3639fdfa888ed:advanced_api_project/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:django_blog/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
>>>>>>>> 01a850dae2c214b543d28b8224f3639fdfa888ed:advanced_api_project/asgi.py

application = get_asgi_application()
