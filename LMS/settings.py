import os


from pathlib import Path
import dj_database_url

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#cloudinary imports
import cloudinary
import cloudinary.uploader
import cloudinary.api



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY=os.environ.get("SECRET_KEY")
SECRET_KEY="dskfjkdslaj,xfkjdkslaiu2435433333eqq309"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =os.environ.get("DEBUG","False").lower=="true"

#ALLOWED_HOSTS =os.environ.get("ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS =['technokraftz.com', 'www.technokraftz.com']


#CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split('')
CSRF_TRUSTED_ORIGINS = ['technokraftz.com', 'www.technokraftz.com']



# SECURE_SSL_REDIRECT = \
#     os.getenv('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']
# if SECURE_SSL_REDIRECT:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'app',
    'user',
    'photo',
    'bootstrap4',
    'crispy_forms',
    'cloudinary',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'app.middleware.AdBlockerMiddleware',
    #'django.contrib.staticfiles.middleware.StaticFilesMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'LMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#database_url=os.environ.get("DATABASE_URL")
#DATABASES['default']=dj_database_url.parse(database_url)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'technokraftzonline-database',
#         'HOST': 'technokraftzonline-server.postgres.database.azure.com',
#         'USER': 'xhzjzieman',
#         'PASSWORD': 'FO16A4AM85F2ZWR5$',
#         'OPTIONS': {'sslmode': 'require'},
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#static_or_media_list=['/static/', '/media/']
# static_files_list=[os.path.join(BASE_DIR, 'static')]
# settings.py

# Define the URL prefix for static files
#STATIC_URL = 'static/'

# Define the directories where static files are located
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_root')]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# MEDIA_URL=static_or_media_list[1]
# MEDIA_ROOT=MEDIA_URL
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

AUTHENTICATION_BACKENDS = [
#    'app.emailBackend.EmailBackEnd',
#    # Add other authentication backends if needed
    'django.contrib.auth.backends.ModelBackend',  # Default backend for username/password authentication
]

ADMIN_URL="supersecret/"
#AUTH_USER_MODEL = 'app.User'

JAZZMIN_SETTINGS={
    "site_header":"Technokraftz Academy",
    "site_brand":"Technokraftz",
    "site_logo":"assets/img/technok/technok.png",
    "copyright":"All Right Reserved, Copyright 2023-Till Date",
    "order_with_respect_to":["Technokraftz"]
}
LOGIN_REDIRECT_URL = 'home'
# LOGIN_URL='login/'
#LOGOUT_REDIRECT_URL = 'login'
AUTH_USER_MODEL = 'auth.User'




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mailhog'  # Use the service name defined in docker-compose.yml
EMAIL_PORT = 1025  # The SMTP port exposed by MailHog


CRISPY_TEMPLATE_PACK = 'bootstrap4'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#CSRF_TRUSTED_ORIGINS= ['https://technokraftzonline.azurewebsites.net', 'https://technokraftz.com', 'http://technokraftz.com']


#Cloudinary - Django integration

cloudinary.config(
    cloud_name="diso33vtf",
    api_key="994881855294481",
    api_secret="pcd6yLrPrD0SrMmUPvY9EypzDvY",
)

