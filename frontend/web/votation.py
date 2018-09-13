import dbmanager
import sqlite3
import config
import re
from datetime import date
import user

class votation_dto:
    """DTO class for the database table"""
    def __init__(self):
        self.votation_id = None
        self.promoter_user_id = None
        self.votation_description = None
        self.begin_date = None
        self.end_date = None
        self.votation_type = None 

def get_blank_dto():
    v = votation_dto()
    v.votation_id = ''
    v.promoter_user_id = 0
    v.votation_description = ''
    v.begin_date = ''
    v.end_date = ''
    v.votation_type = ''
    return v 
    

def load_votation_by_id(votation_id):
    """Returns a votation_dto object or None"""
    v = None
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select * from votation where votation_id = ?", (votation_id,) )
    row = c.fetchone()
    if row:
        v = votation_dto()
        v.votation_id = row['votation_id']
        v.promoter_user_id = row['promoter_user_id']
        v.votation_description = row['votation_description']
        v.begin_date = row['begin_date']
        v.end_date = row['end_date']
        v.votation_type = row['votation_type']
    c.close()
    conn.close()
    return v


def load_votations():
    """Returns a votation_dto array"""
    ar = []
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select * from votation" )
    row = c.fetchone()
    while row:
        v = votation_dto()
        v.votation_id = row['votation_id']
        v.promoter_user_id = row['promoter_user_id']
        v.votation_description = row['votation_description']
        v.begin_date = row['begin_date']
        v.end_date = row['end_date']
        v.votation_type = row['votation_type']
        ar.append(v)
        row = c.fetchone()
    c.close()
    conn.close()
    return ar

def load_votations_by_promoter_user_id(promoter_user_id):
    """Returns a votation_dto array"""
    ar = []
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select * from votation where promoter_user_id = ?", (promoter_user_id,) )
    row = c.fetchone()
    while row:
        v = votation_dto()
        v.votation_id = row['votation_id']
        v.promoter_user_id = row['promoter_user_id']
        v.votation_description = row['votation_description']
        v.begin_date = row['begin_date']
        v.end_date = row['end_date']
        v.votation_type = row['votation_type']
        ar.append(v)
        row = c.fetchone()
    c.close()
    conn.close()
    return ar

def insert_votation_dto(v):
    """Insert the votation_dto into the DB"""   
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("""insert into votation(
                    votation_id, 
                    promoter_user_id, 
                    votation_description, 
                    begin_date, 
                    end_date, 
                    votation_type) values(?,?,?,?,?,?)""",(v.votation_id, v.promoter_user_id, v.votation_description, v.begin_date, v.end_date, v.votation_type) )
    c.close()
    conn.close()
        
def delete_votation_by_id(votation_id):
    """Delete the votation from the DB"""    
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("delete from votation where votation_id = ?", (votation_id,))
    c.close()
    conn.close()

def validate_dto(v):
    """Validate data for writing in DB. Returns (True/False, "Error message")"""
    result = True
    errorMessage = "Data validated"
    if result:
        if not validate_votation_id(v.votation_id):
            result = False
            errorMessage = "Votation id not valid"
    if result:
        if user.load_user_by_id(v.promoter_user_id) == None:
            result = False
            errorMessage = "Promoter user id not valid"
    if result:
        if len(v.votation_description.strip()) == 0:
            result = False
            errorMessage = "Description is mandatory"
    if result:
        if not validate_string_date(v.begin_date):
            result = False
            errorMessage = "Begin date not valid"
    if result:
        if not validate_string_date(v.end_date):
            result = False
            errorMessage = "End date not valid"
    if result:
        if v.votation_type != 'random' and v.votation_type != 'majority':
            result = False
            errorMessage = "Votation Type not valid"
    if result:
        if load_votation_by_id(v.votation_id):
            result = False
            errorMessage = "Votation Id is a duplicate"
    return (result, errorMessage)
            

def validate_votation_id(votation_id):
    if len(votation_id.strip())==0:
        return False
    match_obj = re.fullmatch("[a-zA-Z0-9.]+", votation_id)
    return match_obj != None

def validate_string_date(d):
    result = True
    try:
        y = int(d[0:4])
        m = int(d[5:7])
        d = int(d[8:10])
        date(y,m,d)
    except:
        result = False
    return result    