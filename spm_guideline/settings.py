from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY ---
# Keep this secret in production!
SECRET_KEY = 'django-insecure-2(mh$5t^=g@l0(r#wvlks#vq1tr9z3)$*^^&x6ezfb-qd^)h#$'

# Set to False in production
DEBUG = True

# Allows local development access
ALLOWED_HOSTS = ['*']

# --- AUTHENTICATION URLS ---
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'jazzmin',  # Jazzmin must be above django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party Apps
    'rest_framework',
    'corsheaders',  # Essential for JS fetch() requests to work
    
    # Local Apps
    'main',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be as high as possible
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spm_guideline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'spm_guideline.wsgi.application'

# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- REST FRAMEWORK & CORS ---
# Required for both myScript2.js (Scholarships) and pathwayScript.js (Pathway Hub)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

# Allows the browser to fetch API data without security blocks
CORS_ALLOW_ALL_ORIGINS = True 

# --- STATIC & MEDIA FILES ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/ 'main'/ 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Essential for showing university and scholarship logos
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- JAZZMIN ADMIN SETTINGS ---
JAZZMIN_SETTINGS = {
    "site_title": "SPM Guideline Admin",
    "site_header": "SPM Guideline Management",
    "site_brand": "SPM Admin",
    "welcome_sign": "Welcome to Admin Dashboard",
    "copyright": "SPM Guideline Team",
    "search_model": ["main.Scholarship", "main.PathwayHub"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Main Website", "url": "/", "new_window": True},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-primary navbar-dark",
    "accent": "accent-primary",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
}