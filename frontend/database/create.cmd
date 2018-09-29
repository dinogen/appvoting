@echo off
del voting.sqlite3.db
sqlite3 voting.sqlite3.db < create.sql
copy voting.sqlite3.db \opt\voting\database
pause
