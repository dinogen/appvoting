import dbmanager
import sqlite3
import config
import re
from datetime import date
import user

STATUS_WAIT_FOR_CAND_AND_GUAR = 0
STATUS_WAIT_FOR_GUAR_HASHES = 1
STATUS_WAIT_FOR_CAND_KEYS = 2
STATUS_WAIT_FOR_GUAR_KEYS = 3
STATUS_CALCULATION = 4
STATUS_ENDED = 5
STATUS_FAILED = 6
TYPE_RANDOM = 'random'
TYPE_MAJORITY = 'majority'
states = [
    "Waiting for candidates and guarantors",
    "Waiting for guarantors passphrases",
    "Waiting for candidates passphrases",
    "Waiting for guarantors confirming passphrases",
    "Elaborating, please wait...",
    "Ended",
    "Failed",
]


class votation_dto:
    """DTO class for the database table"""

    def __init__(self):
        self.votation_id = None
        self.promoter_user = user.user_dto()
        self.votation_description = None
        self.begin_date = None
        self.end_date = None
        self.votation_type = None
        self.votation_status = None


def get_blank_dto():
    v = votation_dto()
    v.votation_id = 0
    v.promoter_user.user_id = 0
    v.votation_description = ''
    v.begin_date = ''
    v.end_date = ''
    v.votation_type = ''
    v.votation_status = 0
    return v


def load_votation_by_id(votation_id):
    """Returns a votation_dto object or None"""
    v = None
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select * from votation where votation_id = ?", (votation_id,))
    row = c.fetchone()
    if row:
        v = votation_dto()
        v.votation_id = row['votation_id']
        v.promoter_user = user.load_user_by_id( row['promoter_user_id'] )
        v.votation_description = row['votation_description']
        v.begin_date = row['begin_date']
        v.end_date = row['end_date']
        v.votation_type = row['votation_type']
        v.votation_status = row['votation_status']
    c.close()
    conn.close()
    return v


def load_votations():
    """Returns a votation_dto array"""
    ar = []
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("select * from votation")
    row = c.fetchone()
    while row:
        v = votation_dto()
        v.votation_id = row['votation_id']
        v.promoter_user = user.load_user_by_id( row['promoter_user_id'] )
        v.votation_description = row['votation_description']
        v.begin_date = row['begin_date']
        v.end_date = row['end_date']
        v.votation_type = row['votation_type']
        v.votation_status = row['votation_status']
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
    c.execute("select * from votation where promoter_user_id = ?",
              (promoter_user_id,))
    row = c.fetchone()
    while row:
        v = votation_dto()
        v.votation_id = row['votation_id']
        v.promoter_user = user.load_user_by_id(row['promoter_user_id'])
        v.votation_description = row['votation_description']
        v.begin_date = row['begin_date']
        v.end_date = row['end_date']
        v.votation_type = row['votation_type']
        v.votation_status = row['votation_status']
        ar.append(v)
        row = c.fetchone()
    c.close()
    conn.close()
    return ar


def insert_votation_dto(v):
    """Insert the votation_dto into the DB"""
    result = True
    #try:
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("""insert into votation(
                    promoter_user_id, 
                    votation_description, 
                    begin_date, 
                    end_date, 
                    votation_type,
                    votation_status) values(?,?,?,?,?,?)""", (v.promoter_user.user_id, v.votation_description, v.begin_date, v.end_date, v.votation_type, v.votation_status))
    v.votation_id = c.lastrowid
    c.close()
    conn.close()
    #except sqlite3.IntegrityError::
    #    print(e)
    #    result = False
    return result


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
        if user.load_user_by_id(v.promoter_user.user_id) == None:
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
        if v.end_date < v.begin_date:
            result = False
            errorMessage = "Begin and End dates are not in sequence"
    if result:
        if v.votation_type != TYPE_RANDOM and v.votation_type != TYPE_MAJORITY:
            result = False
            errorMessage = "Votation Type not valid"
    if result:
        if v.votation_status < STATUS_WAIT_FOR_CAND_AND_GUAR or v.votation_status > STATUS_FAILED:
            result = False
            errorMessage = "Status not valid: {}".format(v.votation_status)
    return (result, errorMessage)


def validate_string_date(d):
    result = True
    try:
        y = int(d[0:4])
        m = int(d[5:7])
        d = int(d[8:10])
        date(y, m, d)
    except:
        result = False
    return result


def update_status(votation_id, new_status):
    conn = dbmanager.get_connection()
    c = conn.cursor()
    c.execute("update votation set votation_status=? where votation_id = ?", (new_status,votation_id,))
    c.close()
    conn.close()


    
