# users/permissions.py
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permission pour accéder aux vues uniquement pour l'admin.
    """
    def has_permission(self, request, view):
        return request.user.is_admin


class IsBank(permissions.BasePermission):
    """
    Permission pour accéder aux vues uniquement pour le kiosque bancaire.
    """
    def has_permission(self, request, view):
        return request.user.is_bank


class IsBoutique(permissions.BasePermission):
    """
    Permission pour accéder aux vues uniquement pour la boutique.
    """
    def has_permission(self, request, view):
        return request.user.is_boutique
