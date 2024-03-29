"""
Django settings for developer_box project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^()s1btwg8h81#x#avl$w@4$yg6l$k35u_8-@usuvbo)e8fi))'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

TEMPLATE_DIRS = (
  os.path.join(BASE_DIR, 'templates'),
)

ADMINS = (
    ('Nick Hagianis', 'nhagianis@gmail.com'),
)
MANAGERS = ADMINS


# Update this later
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
  'threadedcomments',
  'django.contrib.comments',
  'storages',
  'south',
  'registration',
  'rest_framework',
  'django.contrib.admin',
  'compressor',
  'debug_toolbar',
  'developer_box'
)

SITE_ID = 1

COMMENTS_APP = 'threadedcomments'

ACCOUNT_ACTIVATION_DAYS = 7

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)


AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'developer_box.backends.auth_backend.UsernameEmailBackend',
)


INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'developer_box.urls'

WSGI_APPLICATION = 'developer_box.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.sqlite3',
  'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder',
)

LOGIN_REDIRECT_URL = '/accounts/profile'


STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'developer_box/static_files'),
)

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    #'DEFAULT_MODEL_SERIALIZER_CLASS':
        #'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        # needs security bugs worked out
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'PAGINATE_BY': 10
}

try:
  # create a local settings file for local testing with at least the following
  # DEBUG = True
  # TEMPLATE_DEBUG = True
  # STATIC_ROOT = 'developer_box/static'
  # STATIC_URL = '/static/'
  from local_settings import *
except ImportError:
  # PRODUCTION SETTINGS
  # static file storage and service
  AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
  AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
  AWS_QUERYSTRING_AUTH = False
  AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
  STATIC_URL = S3_URL
  COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  #COMPRESS_OFFLINE = True
  COMPRESS_ENABLED = False
  #email service
  EMAIL_HOST = 'smtp.sendgrid.net'
  EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
  EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True

  # Parse database configuration from $DATABASE_URL
  import dj_database_url
  DATABASES['default'] =  dj_database_url.config()
  # Honor the 'X-Forwarded-Proto' header for request.is_secure()
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



