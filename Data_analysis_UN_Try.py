#!C:/Python27

import csv
import ast
import matplotlib.pyplot as plt
from matplotlib import axis as ax
import numpy as np
# plt.close('all')

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        if height != 0:
		    plt.text(rect.get_x()+rect.get_width()/2., 1.0*height, '%d'%int(height),
	                ha='center', va='bottom')
#
#
#Inputing data from CSV and making different variables for DATA visualization
#

def PlottingData(Index,RadioData,x_label,y_label,title):
	plt.figure();
	width = 0.5
	RadioDataPlot = plt.bar(Index,RadioData,width,color = 'b')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	plt.ylim(ymax = max(RadioData) + max(RadioData)*0.05)
	print Index
	# plt.xlim(xmax = len(Index)+5)
	xticks_pos = [0.5*patch.get_width() + patch.get_xy()[0] for patch in RadioDataPlot]
	# xtickx_pos = np.arange(min(Index)+1,len(Index)+min(Index)+1)
	plt.xticks(xticks_pos,Index)
	# Index = set(map(str,Index))
	# set(gca,'Xtick',1:5,'XTickLabel',Index)
	# axis = plt.Axes(RadioDataPlot,[.1, .1,.8,.8])
	# ax.Axis.set_ticklabels(axis,Index)
	autolabel(RadioDataPlot)
	plt.show()




data = []
with open('Telecommdata_radio.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		data.append(row)
header = data[0]
# print len(data)
CountryName = []
Index = []
RadioData = []
Year = []

for i in xrange(1,len(data)):
	CountryName.append(str(data[i][1]))
	Index.append(int(data[i][0]))
	if data[i][3] != '':
		Year.append(ast.literal_eval(data[i][3]))
	else:
		Year.append('NA')
	if data[i][2] != '...':
		RadioData.append(ast.literal_eval(data[i][2]))
	else:	
		RadioData.append(0.0)
Years = list(set(Year))
Years = Years[1:len(Years)]
# print len(RadioData)
RadioDataSum = [0] * (len(Years))
ind = 0
for year in Years:
	for i in xrange(1,len(data)-1):
		if Year[i] == year and year != 'NA':
			RadioDataSum[ind] = RadioDataSum[ind] + RadioData[i]
	if year != 'NA':
		ind = ind + 1

print RadioDataSum
# print Years
# print min(Index)

# 
# ######################
# Data Visualization
# ######################
# 
# PlottingData(Index,RadioData,'Index of Countries','Radio in Household(Zeros for data not present)','Radio Data from 2008-2012')
PlottingData(Years,RadioDataSum,'Years','Cumulative Radio according to years','Cumulative Radio Data from 2008-2012')

# fig,ax = plt.subplots()
# ax.set_xlabel('Country Index')
# ax.set_ylabel('Radio in Household(Zeros for data not present)')
# ax.set_title('Radio Data from 2008-2012')
# RadioDataPlot = ax.bar(Index,RadioData,0.15,color='r')
# ax.ylim(ymax = 110)
# ax.set_xticks(range(len(RadioData)))
# ax.set_xticklabels()
# plt.xticks(range(len(Index)),CountryName,size= 'small')

# plt.close()