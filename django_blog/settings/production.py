
from .base import *



# SECURITY WARNING: don't run with debug turned on in production!


DEBUG = True

ALLOWED_HOSTS = [
    'bootstrapblog1.herokuapp.com',
  
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'d7841ipoh2bco6',
        'USER':'intbreerpnutce',
        'PASSWORD':'4cc43b06d35f906d383aac8aa230aba71c293d7d5e95cfe38b606a702e8b4898',
        'HOST':'ec2-18-215-99-63.compute-1.amazonaws.com',
        'POST':5432,
    }
}

STATICFILES_DIRS=(BASE_DIR,'static')