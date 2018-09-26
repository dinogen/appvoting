import hashlib
import os.path
import subprocess as sp
import config

HEXSTRING_LEN_GUAR = 55
HEXSTRING_LEN_CAND = 48

def string2hex(key, key_length):
    if key == None:
        return None
    s = key.ljust(key_length)
    result = ''
    for c in s:
        result = "%s%0.2X" % (result, ord(c))
    return result

def create_election(votation_id, candidates_n, guarantors_n):
    """Backend program Creation"""
    election_dir = os.path.join(config.ELECTIONPATH, "election{}".format(votation_id))
    cp = sp.run([os.path.join(config.BINPATH,"Creation"), election_dir, str(candidates_n), str(guarantors_n)], stdout=sp.PIPE)
    control_string = "Election successfully created with {} candidates and {} guarantors".format(candidates_n, guarantors_n)
    # print(control_string)
    # print(str(cp.stdout))
    if cp.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def guarantor_send_hash(votation_id, user_id, hash_key):
    """Backend program Start"""
    return True

def candidate_send_passphrase(votation_id, user_id, passphrase):
    """Backend program Vote"""
    return True

def guarantor_confirm_passphrase(votation_id, user_id, passphrase):
    """Backend program CLose"""
    return True

