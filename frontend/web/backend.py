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

def election_dir(votation_id):
    election_dir = os.path.join(config.ELECTIONPATH, "election{}".format(votation_id))
    return election_dir


def create_election(votation_id, candidates_n, guarantors_n):
    """Backend program Creation"""
    cp = sp.run([os.path.join(config.BINPATH, "Creation"), election_dir(votation_id), str(candidates_n), str(guarantors_n)], stdout=sp.PIPE)
    control_string = "Election successfully created with {} candidates and {} guarantors".format(candidates_n, guarantors_n)
    # print(control_string)
    # print(str(cp.stdout))
    if cp.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def guarantor_send_hash(votation_id, guar_n, passphrase):
    """Backend program Start"""
    # TODO il user_id deve essere sostituito con un numero di ordine
    hexword = string2hex(passphrase, HEXSTRING_LEN_GUAR)
    #print("hexword:  " + hexword)
    h = hashlib.sha256()
    h.update(hexword.encode('utf-8'))
    hexstring = h.hexdigest()
    #print("hexstring: "+hexstring)
    cp2 = sp.run([os.path.join(config.BINPATH, "Start"), election_dir(votation_id), str(guar_n), hexstring], stdout=sp.PIPE)
    print("Start: "+ str(cp2.stdout))
    control_string = "Key of guarantor {} set".format(guar_n)
    if cp2.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def candidate_send_passphrase(votation_id, cand_n, passphrase):
    """Backend program Vote"""
    # TODO il user_id deve essere sostituito con un numero di ordine
    hexword = string2hex(passphrase, HEXSTRING_LEN_CAND)
    #print("hexword:  " + hexword)
    cp2 = sp.run([os.path.join(config.BINPATH, "Vote"), election_dir(votation_id), str(cand_n), hexword], stdout=sp.PIPE)
    print("Vote: "+ str(cp2.stdout))
    control_string = "Vote of candidate {} set".format(cand_n)
    if cp2.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

def guarantor_confirm_passphrase(votation_id, guar_n, passphrase):
    """Backend program Close"""
    # TODO il user_id deve essere sostituito con un numero di ordine
    hexword = string2hex(passphrase, HEXSTRING_LEN_GUAR)
    #print("hexword:  " + hexword)
    cp2 = sp.run([os.path.join(config.BINPATH, "Close"), election_dir(votation_id), str(guar_n), hexword], stdout=sp.PIPE)
    print("Close: " + str(cp2.stdout))
    control_string = "Vote of candidate {} set".format(guar_n)
    if cp2.stdout.decode('utf-8').startswith(control_string):
        return True
    else:
        return False

