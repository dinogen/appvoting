rm /opt/voting/database/voting.sqlite3.db
rm -f voting.sqlite3.db
sqlite3 voting.sqlite3.db < create.sql
mkdir -p /opt/voting/database
cp -f voting.sqlite3.db /opt/voting/database/
rm -fr /opt/voting/elections/election*


