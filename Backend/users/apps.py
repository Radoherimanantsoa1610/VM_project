from django.apps import AppConfig

class UsersConfig(AppConfig):
    # Définir le type de champ automatique par défaut pour les modèles
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Le nom de l'application, utilisé par Django pour l'identification de l'app
    name = 'users'
