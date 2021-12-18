import ldap
AUTH_LDAP_SERVER_URI = "ldaps://yourhost"
AUTH_LDAP_CONNECTION_OPTIONS = {
            ldap.OPT_REFERRALS: 0
            }
AUTH_LDAP_BIND_DN = "uid=bind-user,cn=users,dc=osl,dc=local,dc=net"
AUTH_LDAP_BIND_PASSWORD = "yourpass"
LDAP_IGNORE_CERT_ERRORS = True

from django_auth_ldap.config import LDAPSearch

#AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=osl,dc=local,dc=net",
AUTH_LDAP_USER_SEARCH = LDAPSearch("cn=users,dc=osl,dc=local,dc=net",
                                                    ldap.SCOPE_SUBTREE,
                                                    "(uid=%(user)s)")

# You can map user attributes to Django attributes as so
#AUTH_LDAP_USER_ATTR_MAP = {
           #"first_name": "givenName",
           #"last_name": "sn",
           #"email": "mail"
                        #}

from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=osl,dc=local,dc=net", ldap.SCOPE_SUBTREE, "(objectClass=group)")

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

AUTH_LDAP_REQUIRE_GROUP = "cn=netbox-user,cn=groups,dc=osl,dc=local,dc=net"

# Define special user types using groups. Exercise great caution when assigning superuser status.
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=netbox-user,cn=groups,dc=osl,dc=local,dc=net",
    "is_staff": "cn=netbox-user,cn=groups,dc=osl,dc=local,dc=net",
    "is_superuser": "cn=netbox-admin,cn=groups,dc=osl,dc=local,dc=net"
}

AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

# for bebugging
# touch /var/log/django-ldap-debug.log ; chmod 777 /var/log/django-ldap-debug.log
# remove after config working
import logging, logging.handlers

logfile = "/var/log/django-ldap-debug.log"
my_logger = logging.getLogger('django_auth_ldap')
my_logger.setLevel(logging.WARNING)
handler = logging.handlers.RotatingFileHandler(
           logfile, maxBytes=1024 * 500, backupCount=5)
my_logger.addHandler(handler)
