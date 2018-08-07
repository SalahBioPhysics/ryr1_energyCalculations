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
This code is used to submit mcce jobs since we have 50 systems 
"""
 
top_location = '/home/salah/ryr1_energyCalculations/calculations/5t9r/'

def myPlot(ch_energy_list,occ_list):
    
    plt.plot(ch_energy_list,occ_list, 'ro')
    #plt.axis([1, 50, 10.5, 12.5])
    plt.show()

occ_list = []
ch_energy_list = []


for i in range(1,51):
	# get fort.38
	fort38 = top_location + "frame_" +str(i).zfill(2)+'/binding/Ca/100_0/fort.38'
	fort38_lines = open(filename).readlines() 
	for line in fort38_lines:
		line =line.split()
		if line[0] == 'extra':
			for fields in line:
				ch_energy_list.append(fields)
		if line[0] == '_CADMB5102_002':
			for fields in line[1:]:
				occ_list.append(fields)
					


with open("data.txt",'w') as energies:
	for occ_list in nsmallest(1, list_of_occ, key=lambda x: abs(x-0.5)):
		
		if float(occ) == occ_list:
			energies.write("frame_%02d" % (i,)+'\t'+extra[kk+1]+'\t'+str(occ_list)+'\n')
	energies.close()











	

