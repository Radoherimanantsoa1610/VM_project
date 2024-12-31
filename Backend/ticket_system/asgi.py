"""
ASGI config for ticket_system project.

This file configures the ASGI application for handling HTTP requests
and provides a foundation for extending support to WebSocket and other
protocols if needed in the future.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'asgi' application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_system.settings')

# Get the default ASGI application.
django_asgi_app = get_asgi_application()

# Future-proof ASGI configuration (e.g., WebSocket or custom protocols).
# Replace "myapp.routing.websocket_urlpatterns" with your WebSocket routes
# if Django Channels or similar is added later.
try:
    from channels.routing import ProtocolTypeRouter, URLRouter
    from channels.auth import AuthMiddlewareStack

    application = ProtocolTypeRouter({
        "http": django_asgi_app,  # Handles HTTP requests.
        # Uncomment and configure WebSocket routing if needed:
        # "websocket": AuthMiddlewareStack(
        #     URLRouter(
        #         myapp.routing.websocket_urlpatterns
        #     )
        # ),
    })
except ImportError:
    # If channels is not installed, fallback to the default ASGI application.
    application = django_asgi_app
