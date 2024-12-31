from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Vue pour obtenir un utilisateur via QR Code
class UserByQRCodeView(APIView):
    """
    Récupère un utilisateur basé sur le QR code. 
    Ce QR code contient un identifiant unique (par exemple un numéro de téléphone ou un ID client).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, qrcode_id):
        try:
            # Recherche de l'utilisateur à partir du QR code (ici, qrcode_id serait l'ID du client)
            user = get_object_or_404(User, username=qrcode_id)  # On suppose que le QR code contient le 'username'
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)

