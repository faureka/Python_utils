from __future__ import print_function
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pylab as pl
from scipy import stats
import os
import statsmodels.api as sm
from patsy import dmatrices
from statsmodels.sandbox.regression.predstd import wls_prediction_std


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

def printer(collist,no):
	print(collist.head(n=no))

def inputNAN(collist):
	count = 0
	for i in xrange(len(collist)):
		try:
			if str(collist.iloc[i]) == ' ' or str(collist.iloc[i]) == '':
				collist.iloc[i] = np.nan
		except:
			count = count + 1
	return collist		
 

def normdata(collist):
	collist = np.array(collist)
	collist = (collist)/max(collist)
	return collist

GDPdata = pd.read_csv('GDPWB.csv',header = 0)
Mobdata = pd.read_csv('ITWB.csv',header = 0)

years = [str(i) for i in xrange(2000,2014)]

df = {}
mdl = {}
corr = {}
for year in years:
	GDPdata[year] = inputNAN(GDPdata[year])
	# print(GDPdata[year].head())
	Mobdata[year] = inputNAN(Mobdata[year])
	# print(Mobdata[year].head())

	df[year] = pd.DataFrame({'GDP':GDPdata[year],
							'MobileData':Mobdata[year]})
	fccol = (years.index(year))%8
	df[year].dropna()
	try:
		y,X = dmatrices('MobileData ~ GDP',data = df[year],return_type ='dataframe')
		X = sm.add_constant(X)

		mdl[year] = sm.OLS(y,X).fit()
		prstd,iv_l,iv_u = wls_prediction_std(mdl[year])
		
		corr[year] = df[year]['MobileData'].corr(df[year]['GDP'])


		# fig  = plt.figure(facecolor = dark2_colors[fccol])
		# ax = fig.add_subplot(111)
		# # ax.plot(X,y,'bo',label = "True")
		# # ax.plot(X, mdl[year].fittedvalues, color = dark2_colors[2], label="OLS")
		# ax.plot(X,iv_u,'r-.',X,iv_l,'r-.')
		# ax.set_axis_bgcolor(dark2_colors[fccol])
		# sm.graphics.plot_fit(mdl[year],1,ax=ax)

		# plt.savefig('GLSPlot%s'%year,facecolor = fig.get_facecolor())
	except Exception , e:
		print(e)

for year in years:
	print(mdl[year].summary())
	print (mdl[year].params)

# with open('ModelSummary.txt','w+') as f:
# 	for year in years:
# 		f.write(mdl[year].summary)
# 		f.write('\n')
