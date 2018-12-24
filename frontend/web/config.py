import os.path
import os
BASEPATH = os.path.join("/opt","voting")
DBPATH = os.path.join(BASEPATH, "database","voting.sqlite3.db")
BINPATH = os.path.join(BASEPATH, "bin")
ELECTIONPATH = os.path.join(BASEPATH,"elections")

AUTH_METHOD="ldap"

LDAP_SERVER_HOST = os.environ.get('LDAP_SERVER_HOST') # ldap.forumsys.com
LDAP_SERVER_PORT = os.environ.get('LDAP_SERVER_PORT') # 389
LDAP_USER_SEARCH_BASE = os.environ.get('LDAP_USER_SEARCH_BASE') # dc=example,dc=com
LDAP_ROOT_DN = os.environ.get('LDAP_ROOT_DN') 
LDAP_USER_SEARCH_FILTER = os.environ.get('LDAP_USER_SEARCH_FILTER') # uid={}

LDAP_URL = "ldap://{}:{}/".format(LDAP_SERVER_HOST,LDAP_SERVER_PORT)
LDAP_BIND = "{}, {}".format(LDAP_USER_SEARCH_FILTER, LDAP_USER_SEARCH_BASE)
