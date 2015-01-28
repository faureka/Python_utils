#!C:/Python27/
import pandas as pd
import pprint as pp
import numpy as np
import ast
from matplotlib import pyplot,axis,cm,rcParams
import pylab as pl
import os
import statsmodels.api as sm
from patsy import dmatrices

dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.grid'] = False
rcParams['font.size'] = 8
rcParams['patch.edgecolor'] = 'none'

colcodes = ['#1B9E75','#D65D02']

#
########### ************  Function Definitions *********************
#
def inputNAN(coldata):
	# coldata.convert_objects(convert_numeric = True).dtypes
	indData = []
	count = 0
	for i in xrange(len(coldata)):
		if coldata.iloc[i] != '...':
			try:
				coldata.iloc[i]= float(coldata.iloc[i])
				indData.append(i)
			except:
				coldata.iloc[i] = np.nan
		else:
			try:
				coldata.iloc[i] = np.nan
			except:
				count = count + 1		
	return coldata,indData		

def prettyprint(coldata,num):
	pp.pprint(coldata.head(n=num))

def remheader(coldata):
	return coldata[1:len(coldata)-5]

def normplotdata(coldata):
	coldata = np.array(coldata)
	# print coldata.mean()
	return (coldata - coldata.mean())/coldata.std()

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

CompData = data['(HH5)'][1:len(data['(HH5)'])]
MobData = data['(HH10)'][1:len(data['(HH10)'])]
Country = data['Country Name'][1:len(data['Country Name'])]
CompYear = data['Year of latest data (HH5)'][1:len(data['(HH5)'])]
MobYear = data['Year of latest data (HH10)'][1:len(data['(HH10)'])]
GDPCountry = GDPcapitaData['Country or Area']

# GDPCountry = set(GDPCountry)


CompData,indC = inputNAN(CompData)
MobData,indM = inputNAN(MobData)
CompYear,indCY = inputNAN(CompYear)
MobYear,indMY = inputNAN(MobYear)

GDPdata = {}
GDPdataMC = {}
for i in xrange(2,len(GDPCountry)+1,5):
	GDPdata[GDPCountry.iloc[i]] = GDPcapitaData['AVG Value'].iloc[i]
key = GDPdata.keys()


finalData = pd.read_csv('DATAfile.csv',header = 0)
finalData = finalData.dropna()

ycomp, X = dmatrices('Computer ~ GDP ', data=finalData, return_type='dataframe')
ymob , X = dmatrices('Mobile ~ GDP',data = finalData,return_type='dataframe')

mdlcomp = sm.OLS(ycomp,X).fit()
mdlmob = sm.OLS(ymob,X).fit()
# print mdl.summary()
# print mdl.params
fig1 = pyplot.figure(facecolor = dark2_colors[2])
ax1 = fig1.add_subplot(212)
ax2 = fig1.add_subplot(211)
ax1.set_axis_bgcolor(dark2_colors[1])
ax2.set_axis_bgcolor(dark2_colors[0])
sm.graphics.plot_fit(mdlcomp,1,ax = ax1)
sm.graphics.plot_fit(mdlmob,1,ax = ax2)
pyplot.savefig('Computer and Mobile Indicators vs GDP',facecolor=fig1.get_facecolor())




'''
with open('DATAfile.csv','w+') as f:
	f.write('Country Name' + ',' + 'GDP'+','+'Mobile%'+','+'Computer%'+'\n')
	for i in xrange(1,len(CompData)):
		for j in xrange(len(key)):
			if str(data['Country Name'].iloc[i]) == str(key[j]):
				f.write(str(data['Country Name'].iloc[i]) + ',' + str(GDPdata[data['Country Name'].iloc[i]]) + ',' + str(MobData.iloc[i-1]) + ',' + str(CompData.iloc[i-1]) +'\n')	
				GDPdataMC[str(key[j])] = GDPdata[key[j]]







	f.close()			
os.startfile('DATAfile.csv')
'''	 


















