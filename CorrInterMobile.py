#!C:/Python27/
import pandas as pd
import pprint as pp
import numpy as np
import ast
from matplotlib import pyplot,axis,cm

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

data = pd.read_csv('CoreIndicators.csv',header = 2)
data = pd.DataFrame(data)

PopData = pd.read_csv('popdata_avg.csv',header=0)
PopData = pd.DataFrame(PopData)

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
AvgPopData = PopData['2012']

# prettyprint(data['Country Name'],4)
popdata = [0]*len(CountryName)

for i in xrange(len(CountryName)):
	for j in xrange(len(CountryName_pop)):
		if CountryName.iloc[i].lower() == CountryName_pop.iloc[j].lower():
			popdata[i] = AvgPopData.iloc[j]

popdata = popdata / max(popdata)
AvgPopData = pd.DataFrame((popdata) * 1000)

CompData = inputNAN(CompData)
InterData = inputNAN(InterData)
IndexData = inputNAN(IndexData)


CompInterData = pd.DataFrame({'Internet %':InterData,
							'Computer %':CompData })
							# 'Index':IndexData })

print CompInterData['Internet %'].corr(CompInterData['Computer %'])

# # pyplot.figure(\)
# # CompInterData.plot(kind = 'bar')
pyplot.scatter(CompInterData['Internet %'],CompInterData['Computer %'],s = AvgPopData)
pyplot.show()

