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
	fort38 = _5t9r + 'frame_' +str(i).zfill(2)+'/binding/Ca/100_0/fort.38' #type file
	fort38_file = open(fort38).readlines()
	for j in fort38_file:
		line = j.split()
		if line[0] == 'extra': # this is the header
			for value in line[1:]:
				extra_list.append(value)
	        if line[0] == '_CADMB5102_002':
			for value in line[1:]:
				occupancy_list.append(value)			
	myPlot(extra_list,occupancy_list)	






	
