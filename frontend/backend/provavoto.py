import shutil
import os,sys
import subprocess as sp
import stringmanager as sm

PROVADIR = 'prova'
CANDIDATESNUM = 5
GUARANTORSNUM = 3
HEXSTRINGLENGTHG = 55
HEXSTRINGLENGTHC = 48

def run_Start(i):
    word = "G" + str(i)
    hexword = sm.string2hex(word.ljust(HEXSTRINGLENGTHG))
    cp1 = sp.run(["./Hash", hexword], stdout=sp.PIPE)
    #print("Words:", word, hexword, cp1.stdout[15:-2])
    #hash value is: xxx
    print("__")
    print("__ Start ", PROVADIR, str(i), cp1.stdout[15:-2])
    print("__")
    cp2 = sp.run(["./Start", PROVADIR, str(i), cp1.stdout[15:-2]], stdout=sp.PIPE)
    print("Start: Guarantor %d: %s" % (i,cp2.stdout))
    
def run_Vote(i):
    word = "{:<48}".format("C"+str(i))
    hexword = sm.string2hex(word.ljust(HEXSTRINGLENGTHC))
    #cp1 = sp.run(["./Hash", hexword], stdout=sp.PIPE)
    #print("Hash:", word, hexword, cp1.stdout[15:-2])
    #hash value is: xxx
    cp2 = sp.run(["./Vote", PROVADIR, str(i), hexword], stdout=sp.PIPE)
    print("Vote: Candidate %d: %s" % (i,cp2.stdout))
    
def run_Close(i):
    word = "G" + str(i)
    hexword = sm.string2hex(word.ljust(HEXSTRINGLENGTHG))
    #cp1 = sp.run(["./Hash", hexword], stdout=sp.PIPE)
    #print("Words:", word, hexword, cp1.stdout[15:-2])
    #hash value is: xxx
    cp2 = sp.run(["./Close", PROVADIR, str(i), hexword], stdout=sp.PIPE)
    print("Close: Guarantor %d: %s" % (i,cp2.stdout))


if __name__ == '__main__':
    os.system("clear")
    # cancellare la directory di prova
    shutil.rmtree(PROVADIR, ignore_errors=True)

    # Lanciare la creazione della votazione
    cp = sp.run(["./Creation", PROVADIR, str(CANDIDATESNUM), str(GUARANTORSNUM)], stdout=sp.PIPE)
    print("Creation terminata:", cp.stdout)
    if not cp.stdout.startswith(b'Election success'):
        sys.exit(1)
    print("----------------------------------------------------------------------------")
    os.system("./State " + PROVADIR)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    # Scelta parola dei garanti
    for i in range(GUARANTORSNUM):
        run_Start(i+1)

    print("----------------------------------------------------------------------------")
    os.system("./State " + PROVADIR)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # Scelta parola dei candidati
    for i in range(CANDIDATESNUM):
        run_Vote(i+1)
    print("---------------------------------------------------------------------------")
    os.system("./State " + PROVADIR)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # Comunicazione parola dei garanti
    for i in range(GUARANTORSNUM):
        run_Close(i+1)
    print("----------------------------------------------------------------------------")
    os.system("./State " + PROVADIR)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    os.system("./State " + PROVADIR)
