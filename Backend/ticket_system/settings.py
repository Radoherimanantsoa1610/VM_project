import os
from pathlib import Path
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()  # Cette ligne décommente pour charger les variables .env

# Définir le chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

print("BASE_DIR:", BASE_DIR)
print("frontend build path:", os.path.join(BASE_DIR.parent, 'frontend', 'build'))

# Sécurité : Clé secrète et autres paramètres de configuration
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'clé_secrète_par_défaut')  # Remplacer par celle du .env
#DEBUG = os.getenv('DEBUG', 'True') == 'True'  # 'True' ou 'False'
DEBUG = False


# Configuration de la base de données PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'event_management'),  # Par défaut 'event_management'
        'USER': os.getenv('DB_USER', 'postgres'),  # Par défaut 'postgres'
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),  # Par défaut 'postgres'
        'HOST': os.getenv('DB_HOST', 'localhost'),  # Par défaut 'localhost'
        'PORT': os.getenv('DB_PORT', '5432'),  # Par défaut '5432'
    }
}

# Autres configurations
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_client',  # Application pour la gestion des clients et tickets
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
    'ticket_system',
    'corsheaders',
    'django_extensions',
]

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'gestion_client', 'templates'),  # Chemin pour les templates personnalisés
            os.path.join(BASE_DIR, 'frontend', 'build'),  # Répertoire de React situé à l'intérieur de Backend
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration des middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Nécessaire pour les sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Nécessaire pour l'authentification
    'django.contrib.messages.middleware.MessageMiddleware',  # Nécessaire pour les messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Ajoute cette ligne en haut
]

# Gestion des fichiers statiques
STATIC_URL = '/static/'

# Répertoires où Django cherchera les fichiers statiques
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'gestion_client', 'static'),
    os.path.join(BASE_DIR, 'frontend', 'node_modules', 'loglevel', 'demo')  # Ajoutez cette ligne si nécessaire
]

print("STATICFILES_DIRS:", STATICFILES_DIRS)

# Répertoire où collectstatic place les fichiers collectés (en production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# Gestion des fichiers médias (upload par les utilisateurs)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Modèle utilisateur personnalisé
AUTH_USER_MODEL = 'gestion_client.User'

# Hôtes autorisés
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Définir le point d'entrée des URLs du projet
ROOT_URLCONF = 'ticket_system.urls'

# Ajout des variables FRONTEND_STATIC_URL et FRONTEND_STATIC_DIR
FRONTEND_STATIC_URL = '/static/'  # Si tu veux que les fichiers statiques soient accessibles via /static/
FRONTEND_STATIC_DIR = BASE_DIR.parent / 'frontend' / 'build' / 'static'  # Correctement répertoir du frontend

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend local
]

CORS_ALLOW_ALL_ORIGINS = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',   # Cherche les fichiers dans les répertoires définis dans STATICFILES_DIRS
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', # Cherche dans les répertoires 'static' des applications
    'django.contrib.staticfiles.finders.DefaultStorageFinder', # Cherche dans le stockage par défaut (généralement pour les fichiers collectés)
]

if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'