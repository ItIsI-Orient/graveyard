
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ddcz',
        'USER': 'root',
        'HOST': 'db',
        'PASSWORD': 'docker',
        'OPTIONS': {
            'charset': 'latin2'
        },
        'TEST': {
            'NAME': 'test_dracidoupe_cz',
            'CHARSET': 'latin2',
        }
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
