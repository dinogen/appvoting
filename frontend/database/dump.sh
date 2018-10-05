cp create.sql create.sql.old
sqlite3 /opt/voting/database/voting.sqlite3.db .dump > create.sql

