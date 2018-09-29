import shutil
import os,sys
import subprocess as sp
import stringmanager as sm

PROVADIR = 'prova'
CANDIDATESNUM = 3
GUARANTORSNUM = 3
HEXSTRINGLENGTHG = 55
HEXSTRINGLENGTHC = 48

def run_Start(i):
    word = "G" + str(i)
    hexword = sm.string2hex(word.ljust(HEXSTRINGLENGTHG))
    cp1 = sp.run(["./Hash", hexword], stdout=sp.PIPE)
    #print("Words:", word, hexword, cp1.stdout[15:-2])
    #hash value is: xxx
    # cp2 = sp.run(["./Start", PROVADIR, str(i), cp1.stdout[15:-2]], stdout=sp.PIPE)
    cp2 = sp.run(["./Start", PROVADIR, str(i), cp1.stdout[15:-2]])
    
def run_Vote(i):
    word = "{:<48}".format("C"+str(i))
    hexword = sm.string2hex(word.ljust(HEXSTRINGLENGTHC))
    #cp1 = sp.run(["./Hash", hexword], stdout=sp.PIPE)
    #print("Hash:", word, hexword, cp1.stdout[15:-2])
    #hash value is: xxx
    cp2 = sp.run(["./Vote", PROVADIR, str(i), hexword])
    
def run_Close(i):
    word = "G" + str(i)
    hexword = sm.string2hex(word.ljust(HEXSTRINGLENGTHG))
    #cp1 = sp.run(["./Hash", hexword], stdout=sp.PIPE)
    #print("Words:", word, hexword, cp1.stdout[15:-2])
    #hash value is: xxx
    cp2 = sp.run(["./Close", PROVADIR, str(i), hexword])


if __name__ == '__main__':
    os.system("clear")
    # cancellare la directory di prova
    shutil.rmtree(PROVADIR, ignore_errors=True)

    # Lanciare la creazione della votazione
    cp = sp.run(["./Creation", PROVADIR, str(CANDIDATESNUM), str(GUARANTORSNUM)])
    #if not cp.stdout.startswith(b'Election success'):
    #    sys.exit(1)

    # Scelta parola dei garanti
    for i in range(GUARANTORSNUM):
        run_Start(i+1)

    # Scelta parola dei candidati
    for i in range(CANDIDATESNUM):
        run_Vote(i+1)
    # Comunicazione parola dei garanti
    for i in range(GUARANTORSNUM):
        run_Close(i+1)

    os.system("./State " + PROVADIR)
