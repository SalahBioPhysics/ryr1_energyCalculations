#!/usr/bin/python
import sys
import re
import math
import datetime
import os
import re
import matplotlib.pyplot as plt
import time

P1 = 'E3967' # This is point 1 (GLU 3967.B CA)
P2 = 'E5001' # This is point 2 (THR 5001.B CA)

distance_list = [] # y-axis in the plot
list_2 = []        # x-axis in the plot


def myPlot(distance_list):
    
    plt.plot(list_2,distance_list, 'ro')
    plt.axis([1, 50, 10.5, 12.5])
    plt.show()

file_location = "/Users/salah_salah/Dropbox/myGithub/ryr1_energyCalculations/input_data/refined/"


with open('/Users/salah_salah/Dropbox/myGithub/ryr1_energyCalculations/output_data/distance.txt','w') as fp:
    for i in range(1,51):
        
        filename = file_location+str(i).zfill(2)+'_5t9r_norm_psi_Class50_SVD12_bfac290_4.5A_real_space_refined.pdb'
        pdb_lines = open(filename).readlines() 
        for line in pdb_lines:
            fields = line.split()
            if len(fields) > 8:
                if fields[4] == P1 and fields[2] == 'CA':
                    #print (fields)
                    x1 = float(fields[5])
                    y1 = float(fields[6])
                    z1 = float(fields[7])
                if fields[4] == P2 and fields[2] == 'CA':
                    #print (fields)
                    x2 = float(fields[5])
                    y2 = float(fields[6])
                    z2 = float(fields[7])
        v1 = math.pow(x2 - x1,2)
        v2 = math.pow(y2 - y1,2)
        v3 = math.pow(z2 - z1,2)
        distance = math.sqrt(v1+v2+v3)
        distance_list.append(distance)
        list_2.append(i)
        write_line = 'frame_'+str(i).zfill(2)+': distance between '+P1+' and '+P2+'= '+str(round(distance,2))+'\n'
        fp.write(write_line)

    fp.close()






myPlot(distance_list)
print ('Done')



