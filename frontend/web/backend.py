import hashlib
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

def create_election(votation_id, candidates_n, guarantor_n):
    """Backend program Creation"""
    return True

def guarantor_send_hash(votation_id, user_id, hash_key):
    """Backend program Start"""
    return True

def candidate_send_passphrase(votation_id, user_id, passphrase):
    """Backend program Vote"""
    return True

def guarantor_confirm_passphrase(votation_id, user_id, passphrase):
    """Backend program CLose"""
    return True

