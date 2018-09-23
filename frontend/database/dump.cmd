@echo off
copy create.sql create.sql.old
sqlite3 \opt\voting\voting.sqlite3.db .dump > create.sql
pause