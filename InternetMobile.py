#!C:/Python27
'''###Countries with Internet When and how much Mobile Access do they have'''

import csv
import ast
import matplotlib.pyplot as plt
from matplotlib import axis,cm
import numpy as np
# import time

def plottingdata(Mobile,Index,Internet,CountryName):
	ax = plt.subplot()
	col = cm.jet(Index)
	# print col
	# ax.stem(Index,Mobile,linefmt = 'b-',markerfmt = 'ko',basefmt = 'r-')
	IndicatorPlot = ax.plot(Index,Mobile,marker = 'o',markerfacecolor = 'k',markeredgecolor ='r' ,ls = 'NONE')
	# ax.set_xlabel('Index Of countries with Mobile')
	# ax.set_ylim(ymin = -.1,ymax = 1.5)
	# axs = plt.Axes(IndicatorPlot,[.1, .1,.8,.8])
	# ax.Axis.set_ticklabels(axs,Index)
	plt.show()

data = []
with open('CoreIndicators.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		data.append(row)

# print data[2][14]
CountryName = []
Index = []
YearInternet = []
YearMobile = []
Mobile = []
Internet = []
MobileCountry = []
for i in xrange(4,len(data)):
	if data[i][14] != '':
		CountryName.append(data[i][1])
		Index.append(ast.literal_eval(data[i][0]))
		YearInternet.append(ast.literal_eval(data[i][14]))
		Internet.append(ast.literal_eval(data[i][13]))
		# print data[i][19]s
		if data[i][19] != '':
			Mobile.append(ast.literal_eval(data[i][18]))
			MobileCountry.append(1)
		else:
			Mobile.append(0)
			MobileCountry.append(1)

plottingdata(MobileCountry,Index,Internet,CountryName)
# for i in xrange(4,len(data)):

# for i 