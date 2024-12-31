from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client


@receiver(post_save, sender=Client)
def client_created(sender, instance, created, **kwargs):
    """ Action à effectuer après la création d'un client. """
    if created:
        print(f"Un nouveau client a été créé : {instance.nom}")
        # Exemple : envoyer un email ou une notification
