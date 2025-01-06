from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsBank, IsBoutique
from rest_framework.response import Response
from .models import Client, Ticket, Transaction
from django.contrib.auth.decorators import user_passes_test
from .models import User
from django.contrib.auth import authenticate

# Vue pour afficher la page d'accueil
def home(request):
    return render(request, 'home.html')  # Remplace 'home.html' par le template correspondant

# Vue de connexion
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Vérification des identifiants
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        # Si les identifiants sont corrects, on renvoie un token
        return JsonResponse({'access': 'token_simule'})
    else:
        # Si les identifiants sont incorrects
        return JsonResponse({'message': 'Identifiants incorrects'}, status=400)

# Vue pour afficher et acheter un ticket
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # Seuls les utilisateurs authentifiés peuvent acheter un ticket
def ticket_acheter(request):
    if request.method == 'POST':
        # Code pour gérer l'achat du ticket, générer le QR code, et envoyer la confirmation
        pass  # Vous devez compléter cette logique
    return render(request, 'ticket/ticket_form.html')

# Vue pour la confirmation de l'achat de ticket
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Accès à tous les utilisateurs authentifiés
def ticket_acheté(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'ticket/ticket_acheté.html', {'ticket': ticket})

# Vue pour récupérer les informations du client (par numéro de téléphone)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Seuls les utilisateurs authentifiés peuvent accéder aux données client
def get_client(request, numero_telephone):
    client = get_object_or_404(Client, numero_telephone=numero_telephone)
    return render(request, 'client/client_detail.html', {'client': client})

# Vue pour l'historique du client
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Seuls les utilisateurs authentifiés peuvent consulter l'historique
def historique_client(request, numero_telephone):
    client = get_object_or_404(Client, numero_telephone=numero_telephone)
    transactions = Transaction.objects.filter(client=client)
    return render(request, 'client/historique_client.html', {'client': client, 'transactions': transactions})

# Vue pour ravitailler le solde du client (via kiosque de banque)
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsBank])  # Limité au personnel de la banque
def ravitaillement_kiosk(request, numero_telephone):
    # Logique pour ravitailler le solde
    pass  # Vous devez compléter cette logique

# Vue pour vérifier le solde du client (via boutique)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsBoutique])  # Limité au personnel de la boutique
def verifier_solde_boutique(request, numero_telephone):
    client = get_object_or_404(Client, numero_telephone=numero_telephone)
    return JsonResponse({'solde': client.solde})

@api_view(['GET'])
def historique_transaction_banque(request, numero_telephone):
    # Implémentez la logique de la vue ici
    return Response({"message": f"Historique des transactions pour {numero_telephone}"})

@user_passes_test(lambda u: u.is_superuser)  # Limite l'accès aux super-utilisateurs
def dashboard_admin(request):
    total_clients = Client.objects.count()
    total_tickets = Ticket.objects.count()
    recent_transactions = Transaction.objects.order_by('-date')[:5]

    return render(request, 'gestion_client/dashboard_admin.html', {
        'total_clients': total_clients,
        'total_tickets': total_tickets,
        'recent_transactions': recent_transactions,
    })

def statistiques_admin(request):
    # Exemple de logique pour récupérer des statistiques
    total_clients = Client.objects.count()
    total_tickets = Ticket.objects.count()
    recent_transactions = Transaction.objects.order_by('-date')[:5]

    return render(request, 'gestion_client/statistiques_admin.html', {
        'total_clients': total_clients,
        'total_tickets': total_tickets,
        'recent_transactions': recent_transactions,
    })

# Gestion des utilisateurs
def gestion_users(request):
    # Exemple de logique pour afficher la liste des utilisateurs
    users = User.objects.all()  # Assure-toi d'utiliser le bon modèle pour les utilisateurs
    return render(request, 'gestion_client/gestion_users.html', {'users': users})

# Exemple de vue pour retourner des données JSON
def my_view(request):
    data = {'key': 'value'}
    return JsonResponse(data)

# Vue pour afficher les rôles des utilisateurs
def gestion_roles(request):
    roles = [
        {'id': 1, 'name': 'Admin'},
        {'id': 2, 'name': 'User'},
    ]
    return JsonResponse(roles, safe=False)

# Exemple de vue simple
def example_view(request):
    return HttpResponse("C'est un exemple de vue !")

# Vue d'accueil
def index(request):
    return render(request, 'index.html')

# Formulaire de ticket
def ticket_form(request):
    return render(request, 'ticket/ticket_form.html')

# Formulaire de création de client
def client_form(request):
    return render(request, 'client/client_form.html')

def formulaire_view(request):
    return render(request, 'templates/formulaire.html')
