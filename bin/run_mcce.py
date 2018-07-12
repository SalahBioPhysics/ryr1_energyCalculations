#!/usr/bin/python
import sys
import os
import time
import os.path
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import call # This is needed to submit jobs

"""
This code is used to submit mcce jobs since we have 50 systems (now, later we'll have 50*5=250 systems)
"""
 
pdb_files = '/home/salah/amedee/ryr1_energyCalculations/input_data/activation_core/'
destination_runs = '/home/salah/amedee/ryr1_energyCalculations/calculations/'


def change_runprm(runprm,prot,str1,str2,str3,str4):
    lines_ = open(runprm).readlines()
    for line in lines_:
        a = line
        line = line.split()
        #print line[-1]
        create_new = runprm+'2'
        with open(create_new,'a') as prm:
            if len(line) != 0:
                if line[-1] == '(INPDB)':
                    newLine = prot+'   '+line[-1]+'\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_PREMCCE)':
                    newLine = str1+'    '+line[-1]+'\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_ROTAMERS)':
                    newLine = str2+'    '+line[-1]+'\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_ENERGY)':
                    newLine = str3+'    '+line[-1]+'\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_MONTE)':
                    newLine = str4+'    '+line[-1]+'\n'
                    prm.write(newLine)
                else:
                    prm.write(a)

            prm.close()
    sys_call = 'mv ' + create_new + ' ' + runprm
    os.system(sys_call) 
 
for i in range(2,30):
    #onlyfiles = [f for f in os.listdir(pdb_files+topDir) if os.path.isfile(os.path.join(pdb_files+topDir, f))]
    #pdbfile = topDir.split('-')
    mydirectory = destination_runs + "frame_" +str(i).zfill(2)+'/'
    print mydirectory
    if not os.path.exists(mydirectory):
        sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)
    

    if not os.path.exists(mydirectory+'run.prm'): # Make sure the run.prm file is in the directory
        sys_call = 'cp ' + destination_runs+'run.prm '+mydirectory
        os.system(sys_call)

    if not os.path.exists(mydirectory+'submit.sh'): # Make sure the submit.sh file is in the directory
        sys_call = 'cp ' + destination_runs+'submit.sh '+mydirectory
        os.system(sys_call)

    if not os.path.exists(mydirectory+str(i).zfill(2)): # Make sure the input PDB file is in the directory
        sys_call = 'cp ' + pdb_files+str(i).zfill(2)+'.pdb '+mydirectory
        os.system(sys_call)

    # Change the (INPUT) param in run.prm to say the correct file name (str(i).zfill(2)+'.pdb ')
    # 1. runprm: the run.prm file that we will edit
    # 2. prot: the name and location of the PDB file
    # 3. str1, str2, str3 and str4 are true (T) or false (F) flags 
    runprm = mydirectory+'run.prm'
    prot   = mydirectory+str(i).zfill(2)+'.pdb'
    change_runprm(runprm,prot,"T","T","T","T")

    # Send to submit 
    os.chdir(mydirectory)
    qsub_call = "qsub %s"
    call(qsub_call % "submit.sh", shell=True)
    # Wait for 5 seconds, so we don't overwork the queue system
    time.sleep(5)
 
print 'Done'
