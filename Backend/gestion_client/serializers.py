from rest_framework import serializers
from .models import Client, Ticket
import re  # Import pour la validation des numéros de téléphone

class ClientSerializer(serializers.ModelSerializer):
    qr_code_url = serializers.SerializerMethodField()  # Pour renvoyer l'URL du QR code
    ticket_valide = serializers.SerializerMethodField()  # Pour vérifier si le client a un ticket valide

    class Meta:
        model = Client
        fields = ['id', 'nom', 'email', 'numero_telephone', 'qr_code_url', 'solde', 'ticket_valide']

    def get_qr_code_url(self, obj):
        """ Renvoie l'URL du QR code enregistré """
        if obj.qr_code:
            return obj.qr_code.url
        return None

    def get_ticket_valide(self, obj):
        """ Vérifie si le client a un ticket valide """
        today = models.DateField.auto_now_add  # Récupère la date actuelle
        # Vérifie si le client a un ticket valide pour aujourd'hui
        valid_ticket = Ticket.objects.filter(client=obj, date_debut__lte=today, date_fin__gte=today).exists()
        return valid_ticket

    def validate_numero_telephone(self, value):
        """ Validation pour vérifier que le numéro de téléphone est au bon format """
        if not re.match(r'^\+?\d{12,15}$', value):  # Vérifie un format de 12 à 15 chiffres avec ou sans le "+"
            raise serializers.ValidationError("Le numéro de téléphone doit être au format international (12 à 15 chiffres).")
        return value

    def validate_solde(self, value):
        """ Assurez-vous que le solde soit positif """
        if value < 0:
            raise serializers.ValidationError("Le solde ne peut pas être inférieur à zéro.")
        return value

    def validate(self, data):
        """ Validation personnalisée pour vérifier certaines règles """
        if 'ticket_valide' in data and not data['ticket_valide']:
            raise serializers.ValidationError("Le client doit avoir un ticket valide pour certaines actions.")
        return data
