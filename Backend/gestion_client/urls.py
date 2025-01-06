from django.urls import path
from . import views
from users.permissions import IsAdmin, IsBank, IsBoutique  # Import des permissions personnalisées
from django.conf import settings
from django.conf.urls.static import static
from .views import login_user
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Routes pour l'achat de ticket et la gestion des clients
    path('', views.home, name='home'),  # La route pour la page d'accueil
    path('ticket/acheter/', views.ticket_acheter, name='ticket_acheter'),  # Formulaire d'achat de ticket
    path('ticket_achete/<int:ticket_id>/', views.ticket_acheté, name='ticket_acheté'),  # Page de confirmation d'achat

    # Client (pas de session utilisateur pour eux, juste des interactions avec QR code)
    path('client/<str:numero_telephone>/', views.get_client, name='get_client'),  # Vérification des clients via leur numéro de téléphone
    path('client/<str:numero_telephone>/historique/', views.historique_client, name='historique_client'),  # Historique des transactions du client (affiché par les agents)

    # Gestion de la banque (Ravitaillement et vérification du solde via le QR code)
    path('kiosk/banque/ravitaillement/<str:numero_telephone>/', views.ravitaillement_kiosk, name='ravitaillement_kiosk'),
    path('kiosk/banque/historique/<str:numero_telephone>/', views.historique_transaction_banque, name='historique_transaction_banque'),

    # Gestion des boutiques (Pas d'accès direct au solde client, mais vérification pour acheter des articles)
    path('kiosk/boutique/verifier_solde/<str:numero_telephone>/', views.verifier_solde_boutique, name='verifier_solde_boutique'),

    # Pour l'admin, gestion des utilisateurs, des événements, etc.
    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('admin/statistiques/', views.statistiques_admin, name='statistiques_admin'),
    path('admin/users/', views.gestion_users, name='gestion_users'),  # Seulement accessible par admin
    path('admin/roles/', views.gestion_roles, name='gestion_roles'),  # Seulement accessible par admin
    path('example/', views.example_view, name='example'),
    path('', views.index, name='index'),  # La vue d'accueil
    path('ticket_form/', views.ticket_form, name='ticket_form'),  # Formulaire d'achat de ticket
    path('client_form/', views.client_form, name='client_form'),  # Formulaire de création de client
    path('api/login/', views.login_user, name='login'),
    path('formulaire/', views.formulaire_view, name='formulaire'),
    path('', views.index, name='gestion_client_home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]

# Ajouter la gestion des fichiers statiques pour le backend et le frontend
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Servir les fichiers médias téléchargés par les utilisateurs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Servir les fichiers statiques du frontend
urlpatterns += static(settings.FRONTEND_STATIC_URL, document_root=settings.FRONTEND_STATIC_DIR)
