from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle étendu pour User avec des rôles
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_bank = models.BooleanField(default=False)
    is_boutique = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='gestion_client_user_set',  # Utilisation d'un nom unique
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='gestion_client_user_permissions_set',  # Utilisation d'un nom unique
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username


# Modèle pour les événements
class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField()
    capacite_max = models.IntegerField()

    def __str__(self):
        return self.nom


# Modèle pour les clients
class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default="Anonymous")
    telephone = models.CharField(max_length=15, unique=True)
    qr_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


# Modèle pour les tickets
class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    date_achat = models.DateField() 
    date_debut = models.DateField()
    date_fin = models.DateField()
    valide = models.BooleanField(default=False)

    def __str__(self):
        return f"Ticket de {self.client} pour {self.evenement}"


# Modèle pour les transactions (recharges ou paiements)
class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='transactions')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_transaction = models.CharField(
        max_length=20,
        choices=[('recharge', 'Recharge'), ('achat', 'Achat')],
    )
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type_transaction.capitalize()} - {self.montant}€ - {self.client}"


# Modèle pour les boutiques
class Boutique(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="boutiques")

    def __str__(self):
        return self.nom
