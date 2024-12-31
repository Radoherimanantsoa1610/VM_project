from django.shortcuts import render, get_object_or_404
from .models import Client, Ticket, Transaction
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsBank, IsBoutique  # Import des permissions

# Vue pour afficher et acheter un ticket
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # Seuls les utilisateurs authentifiés peuvent acheter un ticket
def ticket_acheter(request):
    if request.method == 'POST':
        # Code pour gérer l'achat du ticket, générer le QR code, et envoyer la confirmation
        pass
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
    pass

# Vue pour vérifier le solde du client (via boutique)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsBoutique])  # Limité au personnel de la boutique
def verifier_solde_boutique(request, numero_telephone):
    client = get_object_or_404(Client, numero_telephone=numero_telephone)
    # Logique pour vérifier le solde du client
    return JsonResponse({'solde': client.solde})
