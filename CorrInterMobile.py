#!C:/Python27/
import pandas as pd
import pprint as pp
import numpy as np
import ast
from matplotlib import pyplot,axis,cm

#
########### ************  Function Definitions *********************
#
def inputNAN(coldata):
	coldata.convert_objects(convert_numeric = True).dtypes
	for i in xrange(len(coldata)):
		if coldata.iloc[i] == '...':
			coldata.iloc[i] = np.nan
			# print coldata.iloc[i]
		else:
			coldata.iloc[i]= float(coldata.iloc[i])
		# print coldata.iloc[i]	
	return coldata		

def prettyprint(coldata,num):
	pp.pprint(coldata.head(n=num))

def remheader(coldata):
	return coldata[1:len(coldata)-5]

def normplotdata(coldata):
	return coldata/(sum(coldata)/len(coldata)) * 100

def plotscatter(CompInterData,AvgPopData):
	slope =  CompInterData['Internet %'].corr(CompInterData['Computer %'])
	x = np.linspace(1,100,100,endpoint = False)
	y = slope * x

	fig = pyplot.figure()                                   #Plot figure 1
	ax = fig.add_subplot(111)
#
# ************** Color Properties of Plots
#
	col = cm.jet(np.arange(len(InterData)))
	
#
#
	ax.scatter(CompInterData['Internet %'],CompInterData['Computer %'],s = AvgPopData, c = col)
	ax.plot(y,x,'--r',lw = 1.5)
#
######     Plot properties       ####### 
#
	ax.set_xlabel('% Individual with Internet in a Country')
	ax.set_ylabel('% Individual with Mobile Connectivity')
	ax.set_title('Correlation plot of Internet Connection vs Computer\n(Size of bubble indicates relative population of country)')
	ax.set_axis_bgcolor('k')

def popplot(CountryName_pop,AvgPop):
	x_pop = np.linspace(1,len(CountryName_pop)+1, len(CountryName_pop),endpoint = False)
	meanAvgPop = sum(AvgPop)/len(AvgPop)
	y_pop = [meanAvgPop] * len(x_pop)
	NormAvgPop = normplotdata(AvgPop)
	maxAvgPop = max(NormAvgPop)

	fig1 = pyplot.figure()									#Plot figure 2
	ax1 = fig1.add_subplot(111)
	col_pop = cm.jet(np.arange(len(x_pop)))

	ax1.scatter(x_pop,y_pop , s = NormAvgPop,c = col_pop)
	#
	#######		Plot properties 	########
	#
	ax1.set_xlim(xmin = 0,xmax = len(x_pop) + len(x_pop)*0.05)
	# ax1.set_ylim(ymax = meanAvgPop - maxAvgPop * 0.0005)
	ax1.set_axis_bgcolor('k')

#
### ********************* Reading Data from CSV files ****************
#
data = pd.read_csv('CoreIndicators.csv',header = 2)
data = pd.DataFrame(data)

PopData = pd.read_csv('popdata_avg.csv',header=0)
PopData = pd.DataFrame(PopData)

GDPcapitaData = pd.read_csv('GDPcapita.csv',header = 0)
GDPcapitaData = pd.DataFrame(GDPcapitaData)
#
### ********************** Segregatting data and turning them into columns ********
#
CompData = data['(HH4)']
CompData = remheader(CompData)
# prettyprint(CompData,2)
InterData = data['(HH6)']
InterData = remheader(InterData)
IndexData = data['Index']
IndexData = remheader(IndexData)
CountryName = data['Country Name']
CountryName = remheader(CountryName)
CountryName_pop = PopData['Country Name']
AvgPop = PopData['2012']

#
##############################
#
# prettyprint(data['Country Name'],4)
popdata = [0]*len(CountryName)   								# *** column which hold population data according to country info in first CSV
GDPData = [0]*len(CountryName)


for i in xrange(len(CountryName)):
	for j in xrange(1,len(CountryName_pop)):
		if CountryName.iloc[i].lower() == CountryName_pop.iloc[j].lower():
			popdata[i] = AvgPop.iloc[j]

for i in xrange(len(CountryName)):
	for j in xrange(len(GDPcapitaData['Country or Area'])):
		if CountryName.iloc[i].lower() == GDPcapitaData['Country or Area'].iloc[j].lower():
			GDPData[i] = GDPcapitaData['Value'].iloc[j] + GDPData[i]
		GDPData[i] = GDPData[i] / 5.	
for i in xrange(len(GDPData)):
	if GDPData[i] == 0:
		GDPData[i] = np.nan
# GDPData = GDPData * 0.5

#
#
AvgPopData = pd.DataFrame(normplotdata(popdata))
GDPData = pd.DataFrame({'GDP per Capita':GDPData})
#
### *********** Removing '...' and str and replacing them with NAN to work with Pandas easily
#
CompData = inputNAN(CompData)
InterData = inputNAN(InterData)
IndexData = inputNAN(IndexData)
#
#
#
CompInterData = pd.DataFrame({'Internet %':InterData,
							'Computer %':CompData,
							'Index':IndexData })

#
#
######    Plotting Data 	##############
#
#
# plotscatter(CompInterData,AvgPopData)
# popplot(CountryName_pop,AvgPop)

fig = pyplot.figure()                                   #Plot figure 1
ax = fig.add_subplot(111)
#
# ************** Color Properties of Plots
#
col = cm.jet(np.arange(len(InterData)))

#
#
# ax.scatter(GDPData['GDP per Capita'],CompInterData['Internet %'],s = AvgPopData, c = col)
ax.plot(GDPData['GDP per Capita'],CompInterData['Index'],'--r')
#
################################
pyplot.show()
#
################################

