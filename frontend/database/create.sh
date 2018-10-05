rm -f voting.sqlite3.db
mkdir -p /opt/voting/database
sqlite3 voting.sqlite3.db < create.sql
cp -f voting.sqlite3.db /opt/voting/database
rm -fr /opt/voting/elections/election*


