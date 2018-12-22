import os.path
import os
BASEPATH = os.path.join("/opt","voting")
DBPATH = os.path.join(BASEPATH, "database","voting.sqlite3.db")
BINPATH = os.path.join(BASEPATH, "bin")
ELECTIONPATH = os.path.join(BASEPATH,"elections")
LDAP_URL=os.environ.get('LDAP_URL')
LDAP_BIND=os.environ.get('LDAP_BIND')
AUTH_METHOD="ldap"
