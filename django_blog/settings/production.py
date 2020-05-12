
from .base import *



# SECURITY WARNING: don't run with debug turned on in production!


DEBUG = True

ALLOWED_HOSTS = [
    'bootstrapblog2.herokuapp.com',
  
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'d6fv2nmuh15aiq',
        'USER':'soxglqposhfsxl',
        'PASSWORD':'6871fefef436fffdb660fc6d5d664eda51af9b4c1f6cba7a32bce2fb212e2550',
        'HOST':'ec2-52-202-22-140.compute-1.amazonaws.com',
        'POST':5432,
    }
}

STATICFILES_DIRS=(BASE_DIR,'static')