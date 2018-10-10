rm -f /opt/voting/database/voting.sqlite3.db
mkdir -p /opt/voting/database
sqlite3 /opt/voting/database/voting.sqlite3.db < create.sql
rm -fr /opt/voting/elections/election*


