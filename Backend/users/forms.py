from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Formulaire pour la création d'un nouvel utilisateur.
    Ajoute des widgets pour un meilleur rendu visuel.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez le mot de passe'}),
        }

    def clean_email(self):
        """
        Validation personnalisée pour vérifier l'unicité de l'email.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email


class CustomUserChangeForm(UserChangeForm):
    """
    Formulaire pour la mise à jour d'un utilisateur existant.
    Permet de modifier les informations principales et les droits d'accès.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'is_staff')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_email(self):
        """
        Validation personnalisée pour éviter les doublons lors de la mise à jour.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Cet email est déjà utilisé par un autre utilisateur.")
        return email
