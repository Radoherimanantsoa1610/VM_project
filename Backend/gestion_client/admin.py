from django.contrib import admin
from .models import Evenement, Client, Ticket, Transaction
from django.utils import timezone  # N'oublie pas d'importer timezone pour la validation de la date

# Admin pour Evenement
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_debut', 'date_fin', 'capacite_max')
    search_fields = ('nom',)

# Admin pour Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'qr_code')
    search_fields = ('nom', 'prenom', 'telephone')

# Admin pour Ticket
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('client', 'evenement', 'date_achat', 'date_debut', 'date_fin', 'valide')  # Ajout de date_debut et date_fin
    list_filter = ('valide', 'evenement')

    def valide(self, obj):
        # Vérifie si le ticket est valide en fonction des dates
        return obj.date_debut <= timezone.now().date() <= obj.date_fin

    valide.boolean = True  # Affiche une icône True/False pour la validité du ticket

# Admin pour Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('client', 'montant', 'type_transaction', 'date_transaction')
    list_filter = ('type_transaction', 'date_transaction')
