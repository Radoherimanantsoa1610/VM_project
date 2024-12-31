from django.test import TestCase
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class UserFormTests(TestCase):
    # Test du formulaire de création d'utilisateur valide
    def test_custom_user_creation_form_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertTrue(form.is_valid())  # On s'assure que le formulaire est valide

    # Test du formulaire de création d'utilisateur invalide (email incorrect)
    def test_custom_user_creation_form_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'invalid-email',  # Email incorrect
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertFalse(form.is_valid())  # Le formulaire ne doit pas être valide

    # Test du formulaire de modification d'utilisateur valide
    def test_custom_user_change_form_valid(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='Password123!')
        form = CustomUserChangeForm(instance=user, data={
            'username': 'updateduser',
            'email': 'updated@example.com',
            'is_active': True,
            'is_staff': False,
        })
        self.assertTrue(form.is_valid())  # On s'assure que le formulaire est valide

    # Test du formulaire de modification d'utilisateur invalide (email déjà utilisé)
    def test_custom_user_change_form_invalid(self):
        user1 = User.objects.create_user(username='user1', email='user1@example.com', password='Password123!')
        user2 = User.objects.create_user(username='user2', email='user2@example.com', password='Password123!')
        
        form = CustomUserChangeForm(instance=user1, data={
            'username': 'user1',  # Aucun changement sur le username
            'email': 'user2@example.com',  # Email déjà utilisé
            'is_active': True,
            'is_staff': False,
        })
        
        self.assertFalse(form.is_valid())  # Le formulaire ne doit pas être valide car l'email est déjà pris
        self.assertIn('email', form.errors)  # Vérifier que l'erreur concerne le champ 'email'
