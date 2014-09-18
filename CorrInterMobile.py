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
	return coldata[1:len(coldata)-1]

data = pd.read_csv('CoreIndicators.csv',header = 2)
data = pd.DataFrame(data)


CompData = data['(HH4)']
CompData = remheader(CompData)
# prettyprint(CompData,2)
InterData = data['(HH6)']
InterData = remheader(InterData)
# prettyprint(InterData,2)

CompData = inputNAN(CompData)
InterData = inputNAN(InterData)

CompInterData = pd.DataFrame({'Internet %':InterData,
							'Computer %':CompData	})

print CompInterData['Internet %'].corr(CompInterData['Computer %'])

# pyplot.figure(\)
CompInterData.plot(kind = 'bar')
pyplot.show()

