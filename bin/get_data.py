#!/usr/bin/python
import sys
import os
import time
import os.path
from tempfile import mkstemp
from shutil import move
from os import remove, close

output_data = '/Users/salah_salah/Dropbox/myGithub/ryr1_energyCalculations/output_data/' # Location of data

data_file = output_data+'delta_G.txt'
with open(data_file,'w') as fp1:
	for i in range(1,51): # loop over frames
		fort38 = output_data + "frame_" +str(i).zfill(2)+'/fort.38'
		frame = open(fort38).readlines()
		for line in frame:
			line = line.split()
			for field in line:
				if field == ''
	fp1.close()

