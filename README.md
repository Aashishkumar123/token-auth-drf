# Token Authentication In DRF
Token Authentication is one of the built-in authentication system in Django Rest Framework. Token Authentication is an one time token that is generate for every newly created users, which is unique and static.

<br />

# Let's Setup Token Authentication
## Requirements
Make sure you have already installed these : <br />
1. Python <br />
2. Django <br />
3. Django Rest Framework <br />

To use Token Authentication, you need to add ```'rest_framework.authtoken'``` in ```INSTALLED_APPS```
```
INSTALLED_APPS = [

  'rest_framework.authtoken'

]
```
and also you need to configure the authentication classes to include TokenAuthentication

```
REST_FRAMEWORK = {

     'DEFAULT_AUTHENTICATION_CLASSES': [

             'rest_framework.authentication.TokenAuthentication'

     ]
}
```
Either you can set the TokenAuthentication globally or in a particular view.

You also need to hit the migrate command to successfully create a Token model in database, as rest_framework.authtoken comes with the Token model.
```
python manage.py migrate
```
So, this Token model basically used to store the unique token of a particular user.


If you want to check the Token model in django admin, just open admin.py file and register the Token model.

```
from django.contrib import admin
from rest_framework.authtoken.models import Token

admin.site.register(Token)
```
<br />

<a href="https://pythonworld.io/blogs/how-to-implement-token-authentication-in-django-and-django-rest-framework">Find out the complete blog on Token Authentication</a>



