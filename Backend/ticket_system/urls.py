# ticket_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Route pour l'admin Django
    path('admin/', admin.site.urls),

    # Inclure les routes pour l'API de gestion_client (si tu en as)
    path('api/', include('gestion_client.urls')),

    # Route pour servir l'application React (index.html de React dans le dossier build)
    path('', TemplateView.as_view(template_name='index.html'), name='react-app'),    
]

# Servir les fichiers statiques et médias en mode développement uniquement
if settings.DEBUG:
    # Servir les fichiers statiques du backend (fichiers Django)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Servir les fichiers médias (uploadés par les utilisateurs)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Servir les fichiers statiques du frontend (React)
    urlpatterns += static(settings.FRONTEND_STATIC_URL, document_root=settings.FRONTEND_STATIC_DIR)
     
