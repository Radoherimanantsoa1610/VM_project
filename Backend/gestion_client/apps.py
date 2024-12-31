from django.apps import AppConfig


class GestionClientConfig(AppConfig):
    name = 'gestion_client'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Gestion des Clients'

    def ready(self):
        """ Méthode appelée au démarrage de l'application. """
        from . import signals  # Charger les signaux ici
