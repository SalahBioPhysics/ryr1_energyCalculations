#!/usr/bin/python
import sys
import re
import math
import datetime
import os
import re
import matplotlib
import matplotlib.pyplot as plt
import time
import numpy as np
<<<<<<< HEAD
from heapq import nsmallest
from matplotlib.ticker import FuncFormatter

_5t9r = '/Users/salah_salah/Dropbox/myGithub/ryr1_energyCalculations/output_data/5t9r/'


def myPlot(extra_list,frame_list):
	#y = extra_list
	#x = frame_list   #list(range(1,51)) # This will make a list from 0 to 49
	x = frame_list #np.arange(4)
	energy = extra_list #[1.5e5, 2.5e6, 5.5e6, 2.0e7]
	#formatter = FuncFormatter(millions)

	fig, ax = plt.subplots()
	#ax.yaxis.set_major_formatter(formatter)
	plt.bar(x, energy)
	plt.xlabel('frame')
	plt.ylabel('energy')
	plt.show()
	#formatter = FuncFormatter(millions)


	




	
    	

all_frames_50_50_list = []
all_frames_energy_list = []
def find50_50(extra_list,occupancy_list):
	k = 0
	occ = nsmallest(1, occupancy_list, key=lambda x: abs(x-0.5))
	all_frames_50_50_list.append(occ[0])
	index = occupancy_list.index(occ[0])	
	all_frames_energy_list.append(float(extra_list[index]))

frame_list = []
for i in range(1,51):
	extra_list = []
	occupancy_list = []
	
=======

_5t9r = '/home/guest/ryr1_energyCalculations/calculations/5t9r/'
extra_list = []
occupancy_list = []

def myPlot(extra_list,occupancy_list):
	y = [2,4,6,8,10,12,14,16,18,20]
	x = np.arange(10)
	fig = plt.figure()
	ax = plt.subplot(111)
	ax.plot(x, y, label='$y = numbers')
	plt.title('Legend inside')
	ax.legend()
	#plt.show()
 
	fig.savefig('plot.png')
    	#plt.plot(extra_list,occupancy_list, 'ro')
    	#plt.axis([1, 50, 10.5, 12.5])
    	#plt.show()
    	#plt.savefig('books_read.png')


for i in range(6,51):
>>>>>>> ab305d0df641f64ed48878f7bd344e7668d7e8c3
	fort38 = _5t9r + 'frame_' +str(i).zfill(2)+'/binding/Ca/100_0/fort.38' #type file
	fort38_file = open(fort38).readlines()
	for j in fort38_file:
		line = j.split()
		if line[0] == 'extra': # this is the header
			for value in line[1:]:
				extra_list.append(value)
<<<<<<< HEAD
		if line[0] == '_CADMB5102_002':
			for value in line[1:]:
				occupancy_list.append(float(value))			
	if len(extra_list) == len(occupancy_list):
		frame_list.append(i)
		find50_50(extra_list,occupancy_list)
		#myPlot(extra_list,occupancy_list,i)	
print (frame_list)
print (all_frames_energy_list)
print (all_frames_50_50_list)
myPlot(all_frames_energy_list,frame_list)
=======
	        if line[0] == '_CADMB5102_002':
			for value in line[1:]:
				occupancy_list.append(value)			
	myPlot(extra_list,occupancy_list)	


>>>>>>> ab305d0df641f64ed48878f7bd344e7668d7e8c3




	
