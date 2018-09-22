import dbmanager
import config
import re
from datetime import date
import user
import votation

class guarantor_dto:
    """DTO class for the database table"""
    def __init__(self):
        self.votation_id = None
        self.u = user.user_dto()
        self.hash_ok = None
        self.passphrase_ok = None

def load_guarantor_by_votation(votation_id):
    """Returns a guarantor_dto array"""
    ar = []
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select * from guarantor c where c.votation_id = ?", (votation_id,) )
    row = c.fetchone()
    while row:
        g = guarantor_dto()
        g.votation_id = row['votation_id'] 
        g.hash_ok = row['hash_ok'] 
        g.passphrase_ok = row['passphrase_ok'] 
        g.u = user.load_user_by_id(row['user_id'])
        ar.append(g)
        row = c.fetchone()
    c.close()
    conn.close()
    return ar

def check_for_duplicate(o):
    """Returns true/false"""
    result = False
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select 1 from guarantor where votation_id = ? and user_id=?", (o.votation_id,o.u.user_id) )
    row = c.fetchone()
    if row:
        result = True
    c.close()
    conn.close()
    return result

def insert_dto(o):
    """Insert the guarantor_dto into the DB"""   
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("""insert into guarantor(
                    votation_id, 
                    user_id, hash_ok, passphrase_ok) values(?,?,0,0)""",(o.votation_id, o.u.user_id) )
    c.close()
    conn.close()

error_messages = [
    "", \
    "User undefined", \
    "Votation undefined", \
    "The user id is invalid", \
    "The votation id is invalid", \
    "Duplicate record",
]
        
def validate_dto(o):
    """Validate data for writing in DB. Returns error code, 0 on success"""
    result = 0
    if result==0:
        if o.u.user_id == None:
            result = 1
    if result==0:
        if o.votation_id == None:
            result = 2
    if result==0:
        u = user.load_user_by_id(o.u.user_id)
        if u == None:
            result = 3
    if result==0:
        u = votation.load_votation_by_id(o.votation_id)
        if u == None:
            result = 4
    if result==0:
        if check_for_duplicate(o):
            result = 5
    return result
            
def set_hash_ok(user_id,votation_id):
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("""update guarantor set hash_ok = 1 where 
                    votation_id = ? and
                    user_id = ?""",(votation_id, user_id) )
    c.close()
    conn.close()

