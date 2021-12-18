# netbox_ldap_config
Example ldap config for netbox working with openldap and synology ldap. 

Should work with freeipa with some changes since its based on openldap.

Group layout freeipa.
```
cn=groups,cn=accounts,dc=osl,dc=local,dc=net
```

User layout freeipa
```
cn=youruse,cn=users,cn=accounts,dc=osl,dc=local,dc=net
```



## This is just ldap config file see netbox doc for all config 

Link: https://netbox.readthedocs.io/en/stable/installation/6-ldap/


For ldap auth this should be set in configuration.p

```
REMOTE_AUTH_ENABLED = True
#REMOTE_AUTH_BACKEND = 'netbox.authentication.RemoteUserBackend'
REMOTE_AUTH_BACKEND = 'netbox.authentication.LDAPBackend'
REMOTE_AUTH_HEADER = 'HTTP_REMOTE_USER'
REMOTE_AUTH_AUTO_CREATE_USER = True
REMOTE_AUTH_DEFAULT_GROUPS = []
REMOTE_AUTH_DEFAULT_PERMISSIONS = {}
```
