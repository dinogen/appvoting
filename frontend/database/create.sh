rm -f voting.sqlite3.db
mkdir -p /opt/voting
sqlite3 voting.sqlite3.db < create.sql
cp voting.sqlite3.db /opt/voting/

