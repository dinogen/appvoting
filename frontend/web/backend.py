#import hashlib
import os.path
import subprocess as sp
import config

HEXSTRING_LEN_GUAR = 55
HEXSTRING_LEN_CAND = 48

#MOCK = True
MOCK = False

def string2hex(key, key_length):
    if key == None:
        return None
    s = key.ljust(key_length)
    result = ''
    for c in s:
        result = "%s%0.2X" % (result, ord(c))
    return result

def hash_string(s):
    cp1 = sp.run([os.path.join(config.BINPATH,"Hash"), s], stdout=sp.PIPE)
    return cp1.stdout[15:-2]

def election_dir(votation_id):
    election_dir = os.path.join(config.ELECTIONPATH, "election{}".format(votation_id))
    return election_dir


def create_election(votation_id, candidates_n, guarantors_n):
    """Backend program Creation"""
    if MOCK: return True
    cp = sp.run([os.path.join(config.BINPATH, "Creation"), election_dir(votation_id), str(candidates_n), str(guarantors_n)], stdout=sp.PIPE)
    control_string = "Election successfully created with {} candidates and {} guarantors".format(candidates_n, guarantors_n)
    if cp.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def guarantor_send_hash(votation_id, guar_n, passphrase):
    """Backend program Start"""
    if MOCK: return True
    # TODO il user_id deve essere sostituito con un numero di ordine
    hexword = string2hex(passphrase, HEXSTRING_LEN_GUAR)
    #h = hashlib.sha256()
    #h.update(hexword.encode('utf-8'))
    #hexstring = h.hexdigest()
    hexstring = hash_string(hexword)
    p1 = election_dir(votation_id)
    p2 = str(guar_n)
    p3 = hexstring
    cp2 = sp.run([os.path.join(config.BINPATH, "Start"), p1, p2, p3], stdout=sp.PIPE)
    control_string = "Key of guarantor {} set".format(guar_n)
    if cp2.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def candidate_send_passphrase(votation_id, cand_n, passphrase):
    """Backend program Vote"""
    if MOCK: return True
    # TODO il user_id deve essere sostituito con un numero di ordine
    hexword = string2hex(passphrase, HEXSTRING_LEN_CAND)
    p1 = election_dir(votation_id)
    p2 = str(cand_n)
    p3 = hexword
    cp2 = sp.run([os.path.join(config.BINPATH, "Vote"), p1, p2, p3], stdout=sp.PIPE)
    control_string = "Vote of candidate {} set".format(cand_n)
    if cp2.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def guarantor_confirm_passphrase(votation_id, guar_n, passphrase):
    """Backend program Close"""
    if MOCK: return True
    # TODO il user_id deve essere sostituito con un numero di ordine
    hexword = string2hex(passphrase, HEXSTRING_LEN_GUAR)
    p1 = election_dir(votation_id)
    p2 = str(guar_n)
    p3 = hexword
    cp2 = sp.run([os.path.join(config.BINPATH, "Close"), p1, p2, p3], stdout=sp.PIPE)
    output_string = cp2.stdout.decode('utf-8')
    print(output_string)
    control_string = "Key of guarantor {} set".format(guar_n)
    if output_string.startswith(control_string):
        return True
    else:
        return False

def election_state(votation_id):
    if MOCK: return ["Lorem ipsum dolor sit amet, consectetur adipiscing elit,","sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.","Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."]
    result = []
    p1 = election_dir(votation_id)
    cp = sp.run([os.path.join(config.BINPATH, "State"), p1], stdout=sp.PIPE)
    s =  cp.stdout.decode('utf-8')
    ar = s.split('\n')
    # search for election result:
    is_result = False
    ar_length = len(ar)
    for r in ar:
        if "Election result" in r:
            is_result = True
    if is_result:
        result = [ar[ar_length-6],ar[ar_length-5],ar[ar_length-4],ar[ar_length-3],]
    else:
        result = [ar[ar_length-4],ar[ar_length-3],]

    return result 

def election_ranking(votation_id):
    if MOCK: return [1,2,3,4,5,6]
    result = []
    p1 = election_dir(votation_id)
    cp = sp.run([os.path.join(config.BINPATH, "State"), p1], stdout=sp.PIPE)
    s =  cp.stdout.decode('utf-8')
    ar = s.split('\n')
    # search for election result:
    is_result = False
    ar_length = len(ar)
    for r in ar:
        if is_result and len(r) > 3:
            v = r.split() # 1 2 CHIAVE
            result.append(int(v[1]))
        if "Placement" in r:
            is_result = True
    return result 
