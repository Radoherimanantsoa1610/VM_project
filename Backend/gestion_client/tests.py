from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Client, Ticket
from django.conf import settings

class ClientTestCase(TestCase):

    def setUp(self):
        # Créer un utilisateur de test
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        settings.SECRET_KEY = 'admin_test'

        # Créer un client de test
        self.client_test = Client.objects.create(nom="Test", prenom="User", telephone="1234567890", qr_code="QR1234")

    def test_client_details(self):
        # Test de la vue de détail client (vérifie que l'information du client est bien affichée)
        self.client.login(username='testuser', password='12345')  # Connexion de l'utilisateur pour tester l'accès authentifié
        response = self.client.get(reverse('get_client', kwargs={'numero_telephone': self.client_test.telephone}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')  # Assurez-vous que le nom du client apparaît dans la page

    def test_ticket_acheter(self):
        # Test de la vue pour acheter un ticket (vérification que la page de formulaire se charge)
        self.client.login(username='testuser', password='12345')  # Connexion de l'utilisateur pour tester l'accès authentifié
        response = self.client.get(reverse('ticket_acheter'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket/ticket_form.html')

    def test_historique_client(self):
        # Test de l'historique du client
        self.client.login(username='testuser', password='12345')  # Connexion de l'utilisateur pour tester l'accès authentifié
        Ticket.objects.create(client=self.client_test, evenement="Test Event", date_achat="2024-12-31", date_debut="2024-12-31", date_fin="2024-12-31", valide=True)
        response = self.client.get(reverse('historique_client', kwargs={'numero_telephone': self.client_test.telephone}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_permission_is_authenticated(self):
        # Vérifier que seul un utilisateur authentifié peut accéder à la vue client
        response = self.client.get(reverse('get_client', kwargs={'numero_telephone': self.client_test.telephone}))
        self.assertEqual(response.status_code, 403)  # Non autorisé sans être connecté

        # Tester l'accès en étant authentifié
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('get_client', kwargs={'numero_telephone': self.client_test.telephone}))
        self.assertEqual(response.status_code, 200)  # Accès autorisé après connexion
