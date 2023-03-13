# my_settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'cosmetics',
        'USER': 'root',
        'PASSWORD': '0000',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

SECRET_KEY = 'django-insecure-ib$d_p2xf)xkxr$4ojg3t)$0jg%wtj5x9-!_zv*)ufq&9w&7sy'
