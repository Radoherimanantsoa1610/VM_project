from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gestion_client.urls')),  # API Django pour gestion_client
    path('', TemplateView.as_view(template_name='build/index.html'), name='react-app'),  # React Frontend
]

# Servir les fichiers statiques et médias en mode développement uniquement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
