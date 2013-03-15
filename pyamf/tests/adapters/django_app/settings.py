# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

# The simplest Django settings possible

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = ('adapters',)


SECRET_KEY = '8gwwjf+04zjtgfh*dzr+ukuiiowfk$2ovmarr5g9d@1*555yr3'
SECRET_KEY = 'secret_key'
