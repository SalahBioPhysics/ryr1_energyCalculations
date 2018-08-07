import sys
import os
import time
import os.path
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import call # This is needed to submit jobs

"""
This code is used to submit mcce jobs since we have 50 systems 
"""
 
pdb_files = '/home/guest/ryr1_energyCalculations/input_data/activation_core/'
destination_runs = '/home/guest/ryr1_energyCalculations/calculations/5t9r/'


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
                """elif line[-1] == '(TITR_EX0)':
                    newLine = str5+'    '+line[-1]+'\n'
                    prm.write(newLine)
                elif line[-1] == '(TITR_EX0)':
                    newLine = str5+'    '+line[-1]+'\n'
                    prm.write(newLine)"""
                else:
                    prm.write(a)

            prm.close()
    sys_call = 'mv ' + create_new + ' ' + runprm
    os.system(sys_call) 
 
for i in range(1,51):
    #onlyfiles = [f for f in os.listdir(pdb_files+topDir) if os.path.isfile(os.path.join(pdb_files+topDir, f))]
    #pdbfile = topDir.split('-')
    mydirectory = destination_runs + "frame_" +str(i).zfill(2)+'/binding/'
    if not os.path.exists(mydirectory):
	sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)
    
    #mydirectory = destination_runs + "frame_" +str(i).zfill(2)+'/binding/Ca/'
    #if not os.path.exists(mydirectory): 
        #sys_call = 'mkdir ' + mydirectory
        #os.system(sys_call)
    mydirectory = destination_runs + "frame_" +str(i).zfill(2)+'/binding/Zn/'
    if not os.path.exists(mydirectory): 
        sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)
    mydirectory = destination_runs + "frame_" +str(i).zfill(2)+'/binding/Zn/100_0/'
    if not os.path.exists(mydirectory): 
        sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)
    """if not os.path.exists(mydirectory+'Ca/0_100'): 
        sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)
    if not os.path.exists(mydirectory+'Zn/100_0'): 
        sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)
    if not os.path.exists(mydirectory+'Zn/0_100'): 
        sys_call = 'mkdir ' + mydirectory
        os.system(sys_call)"""
    

    # move submit.sh and run.prm
    sys_call = 'cp ' + destination_runs+'submit.sh '+mydirectory
    os.system(sys_call)
    
    sys_call = 'cp ' + destination_runs+'run.prm '+mydirectory
    os.system(sys_call)

    # move head3.lst, step2out, and energies.opp 
    sys_call = 'cp ' + destination_runs + "frame_" +str(i).zfill(2)+'/head3.lst '+mydirectory
    os.system(sys_call)
    sys_call = 'cp ' + destination_runs + "frame_" +str(i).zfill(2)+'/step2_out.pdb '+mydirectory
    os.system(sys_call)
    sys_call = 'cp ' + destination_runs + "frame_" +str(i).zfill(2)+'/energies.opp '+mydirectory
    os.system(sys_call)

    # Change the (INPUT) param in run.prm to say the correct file name (str(i).zfill(2)+'.pdb ')
    # 1. runprm: the run.prm file that we will edit
    # 2. prot: the name and location of the PDB file
    # 3. str1, str2, str3 and str4 are true (T) or false (F) flags 
    runprm = mydirectory+'run.prm'
    prot   = mydirectory+str(i).zfill(2)+'.pdb'
    change_runprm(runprm,prot,"f","f","f","T")

    # Send to submit 
    os.chdir(mydirectory)
    qsub_call = "qsub %s"
    print 'doing ' + mydirectory+'Ca/100_0'
    call(qsub_call % "submit.sh", shell=True)
    # Wait for 5 seconds, so we don't overwork the queue system
    time.sleep(5)
 
print 'Done'

