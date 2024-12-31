from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Modèle utilisateur personnalisé basé sur AbstractUser.
    Ajoute une contrainte d'unicité pour l'adresse email.
    """
    # Définition du champ 'email' avec une contrainte d'unicité
    email = models.EmailField(
        unique=True,
        max_length=255,  # Limite de taille de l'email à 255 caractères
        error_messages={  # Message d'erreur personnalisé si l'email existe déjà
            'unique': "Un utilisateur avec cet email existe déjà.",
        }
    )

    def __str__(self):
        """
        Représentation textuelle de l'utilisateur.
        Affiche le nom d'utilisateur suivi de l'email.
        """
        return f"{self.username} - {self.email}"
