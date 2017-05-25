import hashlib
import os
import uuid
from configurations import Configuration


def get_secret_key(base_dir='.'):
    def gen_key(key_path):
        with open(key_path, 'w') as key_file:
            key = hashlib.sha512(str(uuid.uuid4()).encode('utf-8')).hexdigest()
            key_file.write(key)
        return key

    path = os.path.join(base_dir, '.secret.key')

    try:
        secret_key = open(path).read()
        assert secret_key, 'Wrong secret key'
    except(IOError, AssertionError):
        secret_key = gen_key(path)
    return secret_key


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Dev(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = get_secret_key(BASE_DIR)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',

        # wymagane przez django-allauth
        'django.contrib.auth',
        'django.contrib.sites',

        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'shelf.apps.ShelfConfig',
        'contact.apps.ContactConfig',
        'rental.apps.RentalConfig',
        'users.apps.UsersConfig',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',

        'allauth.socialaccount.providers.facebook',

        'bootstrap3',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'biblio.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'biblio.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'pl'

    TIME_ZONE = 'Europe/Warsaw'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'public')

    MEDIA_URL = '/upload/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/media')

    LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
        os.path.join(BASE_DIR, 'node_modules'),
        os.path.join(BASE_DIR, 'upload'),
    ]

    AUTH_USER_MODEL = 'users.BiblioUser'

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    SITE_ID = 1

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # po potwierdzeniu emaila
    LOGIN_URL = 'main-page'

    # po zalogowaniu
    LOGIN_REDIRECT_URL = 'main-page'


class Production(Dev):
    DEBUG = False
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    STATIC_URL = '/public/'
    MEDIA_URL = '/public/media/'
