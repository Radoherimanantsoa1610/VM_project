from django.urls import path
from . import views
from .permissions import IsAdmin, IsBank, IsBoutique  # Import des permissions personnalisées

urlpatterns = [
    # Routes pour l'achat de ticket et la gestion des clients
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
]

# Appliquer des permissions sur ces URLs via des vues fonctionnelles
# Exemple de protection dans les vues pour `gestion_users` et `gestion_roles` :
# @permission_classes([IsAdmin])
# def gestion_users(request):
#   pass
