import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-zxq2c&xxakrvq4ftw$-o#z^*c_gz97#w*_8#+1b7-n&$bvt-%*'

DEBUG = True

ALLOWED_HOSTS = [
    "readify-deployment-38fc3c9a9a8c.herokuapp.com",
    "localhost",
    "127.0.0.1",
    "readifydsalgo.netlify.app",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'rest_framework',
    'rest_framework.authtoken',  # ✅ Added for Token Authentication
    'django_extensions',
    'corsheaders',
]

# ✅ Allow frontend to make authenticated requests
CORS_ALLOW_CREDENTIALS = True

# ✅ Ensure CORS is set correctly
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://readifydsalgo.netlify.app",
]

# ✅ Corrected CSRF Trusted Origins (Matches CORS)
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

# ✅ Enable CSRF settings (Improved security)
CSRF_COOKIE_SECURE = True  # Use True for HTTPS in production
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript access
CSRF_COOKIE_SAMESITE = "Lax"  # Better security
SESSION_COOKIE_SECURE = True  # Secure session cookies
SESSION_COOKIE_SAMESITE = "Lax"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # ✅ Moved above CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'readify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'readify.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Fixed static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'  # For production
STATICFILES_DIRS = [
    BASE_DIR / 'store/static',  # For local development
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Improved API Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # ✅ Use Token Authentication
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # ✅ Secured API
    ],
}