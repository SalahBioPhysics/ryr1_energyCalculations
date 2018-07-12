#!/usr/bin/python
import sys
import os
import time
import os.path
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import call # This is needed to submit jobs
 
pdb_files = '/home/salah/amedee/ryr1_energyCalculations/input_data/activation_core/'
destination_runs = '/home/salah/amedee/ryr1_energyCalculations/output_data/mcce_runs/amedee/ryr1_energyCalculations/output_data/mcce_runs/'

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
                    newLine = 'new'+prot+'   '+line[-1]+'\n'
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
     
 
 
for i in range(1,2):
    

    #onlyfiles = [f for f in os.listdir(pdb_files+topDir) if os.path.isfile(os.path.join(pdb_files+topDir, f))]
    #pdbfile = topDir.split('-')
    mydirectory = destination_runs + "frame_" +str(i).zfill(2)
    if not os.path.exists(mydirectory):
        sys_call = 'mkdir ' + destination_runs + pdbfile[0]
        os.system(sys_call)
    #sys_call = 'cd ' + destination_runs + pdbfile[0] + '/'
    #os.chdir(sys_call)
    """for pdb_file in onlyfiles:
        if "_fixed_ph7.4.pdb" in pdb_file:
            #print pdb_file[:4]
            #print pdbfile[0]
            mydirectory = destination_runs + pdbfile[0] + '/'+ pdb_file[:4]
            if not os.path.exists(mydirectory):
                sys_call = 'mkdir ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4] 
                os.system(sys_call)
            sys_call = 'cp ' + pdb_files + topDir + '/' + pdb_file + ' ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]
            os.system(sys_call)
            fname_base = destination_runs + pdbfile[0] + '/' + pdb_file[:4] + '/' + pdb_file
            dirName =  destination_runs + pdbfile[0] + '/' + pdb_file[:4]
            deleteHH(dirName,fname_base)
            sys_call = 'cp /home/salah/johnChodera_project_on_github/mcce-charges/mcce_runs/quick/run.prm ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]
            os.system(sys_call)
            sys_call = 'cp /home/salah/johnChodera_project_on_github/mcce-charges/mcce_runs/quick/submit.sh ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]
                        os.system(sys_call)
            runprm = destination_runs+pdbfile[0]+'/'+pdb_file[:4]+'/run.prm'
            change_runprm(runprm,pdb_file,'t','t','f','f')
            sys_call = 'mv '+destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'/run.prm2 '+ destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'/run.prm'
                        os.system(sys_call)
            mysubmit = destination_runs + pdbfile[0] + '/'+ pdb_file[:4]
            #print mysubmit
            os.chdir(mysubmit)
            qsub_call = "qsub %s"
            call(qsub_call % "submit.sh", shell=True)"""
 
print 'Done'
