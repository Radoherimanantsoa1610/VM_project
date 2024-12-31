from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Personnalisation de l'interface d'administration pour le modèle User.
    Utilise des formulaires personnalisés pour la création et la modification des utilisateurs.
    """
    # Formulaire utilisé pour la création d'un nouvel utilisateur
    add_form = CustomUserCreationForm
    # Formulaire utilisé pour la modification d'un utilisateur existant
    form = CustomUserChangeForm

    # Champs à afficher dans la liste des utilisateurs
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff')
    
    # Champs qui peuvent être utilisés pour filtrer les utilisateurs dans l'interface admin
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    # Champs sur lesquels on peut rechercher dans la liste d'utilisateurs
    search_fields = ('username', 'email')
    
    # Ordre d'affichage des utilisateurs dans la liste (ici, tri par 'id')
    ordering = ('id',)
    
    # Configuration des champs qui seront affichés lors de la consultation ou modification d'un utilisateur
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),  # Informations de base
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),  # Permissions utilisateur
    )
    
    # Configuration des champs à afficher lors de la création d'un utilisateur (ceux qui nécessitent un formulaire spécifique)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Définir les classes CSS pour l'affichage
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),  # Champs à afficher
        }),
    )
