"""
WSGI config for ticket_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Assure-toi que l'environnement utilise les bonnes configurations
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_system.settings')

# Si tu utilises un environnement spécifique de production, tu peux configurer cela ici.
# Par exemple, pour le mode de déploiement, ou si tu utilises un serveur spécifique comme Gunicorn:
# os.environ['DJANGO_SETTINGS_MODULE'] = 'ticket_system.settings.production'

# Appelle le WSGI application callable pour exposer le point d'entrée de l'application
application = get_wsgi_application()
