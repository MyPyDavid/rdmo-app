from .base import * 

'''
A secret key for a particular Django installation. This is used to provide
cryptographic signing, and should be set to a unique, unpredictable value.
'''

SECRET_KEY = get_env_variable('SECRET_KEY')

'''
The list of URLs und which this application available
'''
# ALLOWED_HOSTS_ENV = get_env_variable('ALLOWED_HOSTS').split(', ')

# ALLOWED_HOSTS = ALLOWED_HOSTS_DEFAULT + ALLOWED_HOSTS_ENV if any(ALLOWED_HOSTS_ENV) else ALLOWED_HOSTS_DEFAULT

'''
Allauth configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/allauth.html

Keycloak via allauth:
https://django-allauth.readthedocs.io/en/latest/providers.html#keycloak
'''
USE_ALLAUTH = get_env_variable('USE_ALLAUTH', default=False, var_type='bool')

USE_KEYCLOAK = get_env_variable('USE_KEYCLOAK', default=False, var_type='bool')

if USE_ALLAUTH or USE_KEYCLOAK:
    print('\n===-- AllAuth is enabled --===\n')
    
    ACCOUNT = True
    ACCOUNT_SIGNUP = False
    SOCIALACCOUNT = True
    SOCIALACCOUNT_SIGNUP = True
    SOCIALACCOUNT_AUTO_SIGNUP = True

    INSTALLED_APPS += [
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        # 'allauth.socialaccount.providers.facebook',
        # 'allauth.socialaccount.providers.github',
        # 'allauth.socialaccount.providers.google',
        # 'allauth.socialaccount.providers.orcid',
        # 'allauth.socialaccount.providers.twitter',
        
    ]
    AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')

if USE_KEYCLOAK:
    SOCIALACCOUNT_PROVIDERS = {
        'keycloak': {
            'KEYCLOAK_URL': get_env_variable('KEYCLOAK_SERVER_URL'),
            'KEYCLOAK_REALM': get_env_variable('KEYCLOAK_REALM')
        },
    }
    INSTALLED_APPS += ['allauth.socialaccount.providers.keycloak',]

'''
LDAP, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/ldap.html
'''

# import ldap
# from django_auth_ldap.config import LDAPSearch
#
# PROFILE_UPDATE = False
#
# AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
# AUTH_LDAP_BIND_DN = "cn=admin,dc=ldap,dc=example,dc=com"
# AUTH_LDAP_BIND_PASSWORD = "admin"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ldap,dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
#
# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     'email': 'mail'
# }
#
# AUTHENTICATION_BACKENDS.insert(
#     AUTHENTICATION_BACKENDS.index('django.contrib.auth.backends.ModelBackend'),
#     'django_auth_ldap.backend.LDAPBackend'
# )


'''
Shibboleth, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/shibboleth.html
'''

SHIBBOLETH = get_env_variable('SHIBBOLETH', default=False, var_type='bool')

# PROFILE_UPDATE = False
#
# INSTALLED_APPS += ['shibboleth']
#
# SHIBBOLETH_ATTRIBUTE_MAP = {
#     'uid': (True, 'username'),
#     'givenName': (True, 'first_name'),
#     'sn': (True, 'last_name'),
#     'mail': (True, 'email'),
# }
#
# AUTHENTICATION_BACKENDS.append('shibboleth.backends.ShibbolethRemoteUserBackend')
#
# MIDDLEWARE.insert(
#     MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
#     'shibboleth.middleware.ShibbolethRemoteUserMiddleware'
# )
#
# LOGIN_URL = '/Shibboleth.sso/Login?target=/projects'
# LOGOUT_URL = '/Shibboleth.sso/Logout'


'''
EXPORT_REFERENCE_DOCX
'''
# EXPORT_REFERENCE_DOCX='/srv/rdmo/tu-darmstadt/theme/templates/template_RDMO-TUDA-Design.docx'