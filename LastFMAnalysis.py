#!C:/Python27/
import pandas as pd
import pprint as pp
import numpy as np
import ast
import scipy.stats as st
import re

pattern1 = re.compile('^([^(0-9)-]+|[^\(\)])')
pattern2 = re.compile('[0-9]+')
from matplotlib import pyplot,axis,cm

def prettyprint(coldata,num):
	pp.pprint(coldata.head(n=num))

def regering(coldata):
	for i in xrange(len(coldata)):
		if ord(pattern1.match(coldata[i]).group()[0]) >= 48  and ord(pattern1.match(coldata[i]).group()[0]) <= 57:
			coldata[i] = coldata[i]	
		else:
			coldata[i] = pattern1.match(coldata[i]).group()
	return coldata

def normplotdata(coldata):
	return coldata/(sum(coldata)/len(coldata)) * 100


data = pd.read_csv('LastFMData.csv',header = 0)
data = pd.DataFrame(data)

Track = list(set(data['Track']))

PlayCount = [0] * len(Track)
Artist = ['A'] * len(Track)
Index = [0]*len(Track)

for i in xrange(len(Track)):
	for j in xrange(1,len(data['Track'])):
		if data['Track'].iloc[j] == Track[i]:
			PlayCount[i] = PlayCount[i] +1
			Artist[i] = data['Artist'].iloc[j]
			Index[i] = i

# print PlayCount[11] , Track[11] ,Artist[11]

	
Track = regering(Track)
Artist = regering(Artist)
mPlayCount = sum(PlayCount)/len(PlayCount)
sPlayCount = [0] * len(PlayCount)

for i in xrange(len(PlayCount)):
	sPlayCount[i] = (PlayCount[i] / mPlayCount) * 100
maxPlayCount = max(PlayCount)


# print data['Track].describe
w,p = st.shapiro(PlayCount)

print w,p






# fig = pyplot.figure()                                   #Plot figure 1
# ax = fig.add_subplot(111)
# col = cm.jet(np.arange(len(PlayCount)))
# ax.scatter(Index,PlayCount,s= sPlayCount,color = col)
# tickIndex = []
# tickTrack = []
# for i in xrange(len(PlayCount)):
# 	if PlayCount[i] > maxPlayCount * 0.1:
# 		tickIndex.append(Index[i])
# 		tickTrack.append(Track[i][0:8])

# ax.set_xticks(tickIndex)
# ax.set_xticklabels(tickTrack,rotation = 90)
# ax.set_xlim(xmin = 0)
# ax.set_ylim(ymin = 0)
# ax.set_title('Tracks played over time on Last.FM')
# ax.set_ylabel('Number of time Track is played')
# # ax.set_xlabel('Tracks')
# ax.set_axis_bgcolor('k')
# pyplot.show()
# # pyplot.close(fig)