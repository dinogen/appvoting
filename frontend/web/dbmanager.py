import sqlite3
import config

def get_connection():
    conn = sqlite3.connect(config.DBPATH)
    conn.row_factory = sqlite3.Row
    conn.isolation_level = None # no commit needed
    return conn
