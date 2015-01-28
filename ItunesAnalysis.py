import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import re
from xml.parsers import expat
import plistlib as pl
import csv
#### *******************        plot paramaters **************################
from matplotlib import rcParams

## add these to the plotting for having simple and beautiful plots!
from mpltools import style
from mpltools import layout

style.use('ggplot')

dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 500
# rcParams['axes.color_cycle'] = dark2_colors
# rcParams['lines.linewidth'] = 2
# rcParams['axes.grid'] = False
# rcParams['font.size'] = 8
rcParams['patch.edgecolor'] = 'none'

# colcodes = ['#1B9E75','#D65D02']
############### ******************************   ##############################

def remspecialchar(collist,checkname):
	if checkname == 1:
		OrigName = dict()
		for i in xrange(len(collist)):
			OrigName[collist[i]] = ''
		for i in xrange(len(collist)):
			temp = collist[i]
			collist[i] = ''.join(s for s in collist[i] if s.isalnum())
			OrigName[collist[i]] = temp
		return collist,OrigName


def normdata(collist):
	maxval = max(collist)
	collist = np.array(collist)
	collist = (collist/6000)
	return list(collist)

def csvwrite(trackID):
	count = 0
	head = ['Artist' , 'Track Name' , 'Play Count' , 'Song Duration','\n']
	headers= ['Artist','Name','Play Count','Total Time']
	with open('Itunes.csv','w+') as fout:
	# csv.writer(fout,head)
		for trackid in trackID: 
			# line = [str(data['Tracks'][trackid]['Artist']) , str(data['Tracks'][trackid]['Name']),str(data['Tracks'][trackid]['Play Count']),str(data['Tracks'][trackid]['Total Time']]
			try:
				fout.write(str(data['Tracks'][trackid]['Artist'])+','+str(data['Tracks'][trackid]['Name'])+','+str(data['Tracks'][trackid]['Play Count'])+','+str(data['Tracks'][trackid]['Total Time'])+','+'\n')
			except Exception , e:
				count = count + 1
	fout.close()		
	
def csvread():
	data = pd.read_csv('Itunes.csv',header = 0)
	Artist,OrigArtist = remspecialchar(data['Artist'],1)
	Artist = map(str,Artist)
	TrackName,OrigTrack = remspecialchar(data['Track Name'],1)

	return data,Artist,OrigArtist,TrackName,OrigTrack

def DataInit(data,Artist,OrigTrack,TrackName,OrigArtist):
	indArtist = set()
	dictArtist = dict()
	dictTotalTime = dict()
	dictOrigName = dict()

	for artist in Artist:
		indArtist.add(artist.lower())
	
	for artist in indArtist:
		dictArtist[artist] = 0
		dictTotalTime[artist] = 0
		dictOrigName[artist] = ''

	for i in xrange(len(Artist)):
		for artist in indArtist: 
			if artist == str(Artist[i]).lower():
				dictArtist[artist]	= dictArtist[artist] + int(data['Count'].iloc[i])
				dictTotalTime[artist] = dictTotalTime[artist] + float(data['Total Time'].iloc[i])
				temp = OrigArtist[Artist[i]]
				dictOrigName[artist] = temp	
	
	# NormVal = normdata(dictTotalTime.svalues())
	
	# i = 0
	# for artist in indArtist:
	# 	dictTotalTime[artist] = NormVal[i]
	# 	i = i + 1

	
	Artist_Count = pd.DataFrame({'Artist Name':dictOrigName.values(),
								'Play Count' : dictArtist.values(),
								'Total Time' : dictTotalTime.values()})
	return Artist_Count
				



def PlotData(DataDF):
	'''
	facecolor decided the frame color around the plot

	'''
	fig = plt.figure()                                   #Plot figure 1
	ax = fig.add_subplot(111)
	'''
	Preparing list and variables to plot
	'''
	Index = []
	TotalTime =[]
	playCount =[]
	ArtistName = []
	for i in xrange(len(DataDF['Total Time'])):
		if DataDF['Total Time'].iloc[i] > 150:
			Index.append(i)
			TotalTime.append(DataDF['Total Time'].iloc[i])
			playCount.append(DataDF['Play Count'].iloc[i])
			ArtistName.append(DataDF['Artist Name'].iloc[i])
	
	'''
	Scatter plot is for values which have run time greater a given Threshold
	This Threshold is for the Total Time of the Song played is choosed arbitariraly 
	for now. This has to be passed as  a parameter which needs to be added

	Most of the commands are self explanatory still will try and elaborate on each
	
	'''
	'''
	Scatter plot and Line plot on the same graph
	'''
	ax.scatter(Index,TotalTime,s =playCount)
	ax.plot(DataDF['Total Time'],label = 'Frequency') 						#label shows the Legend on the graph

	'''
	Setting the labels for the X-axis. Not plotting all the values, Clutter the x axis
	'''
	ax.set_xticks(Index)
	ax.set_xticklabels(ArtistName,rotation = 65)
	plt.legend(loc = 'best')												#Decides the position of the legend automagically
	
	'''
	Some more triviality regarding how the plot should look like
	'''
	# ax.set_ylim(ymin = -10)
	# ax.set_xlim(xmin = -5,xmax = len(DataDF['Total Time'])+10)
	'''
	Setting the Background color of the plot
	'''
	# ax.set_axis_bgcolor(dark2_colors[7])

	'''
	Set ylabel and xlabel
	'''

	ax.set_ylabel('Amount of time(min)')
	ax.set_xlabel('Artist')
	# ax.axis('off')
	# ax.yaxis.set_visible(False)

	'''
	Decided to show only the axis which were necesaary that is left and bottom 
	rest can R.I.P. 

	Same happens with the ticks! parasites fucka!! die!! :D
	'''
	# ax.spines['right'].set_visible(False)
	# ax.spines['top'].set_visible(False)
	# ax.xaxis.set_ticks_position('bottom')
	# ax.yaxis.set_ticks_position('left')

	layout.cross_spines(ax = ax)

	'''
	Finally save the image!! Phew
	Too much work just for nothing! :-/
	Well now I know the kind of music my ears love the most :DataDF
	Long live FloyD 
	'''
	# extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
	plt.savefig('Itunes Frequency Analysis.png')
	# plt.show()










def main():
	xml = 'iTunes Music Library.xml'
	data = pl.readPlist(xml)
	trackID = data['Tracks'].keys()
	#csvwrite(trackID)
	data,Artist,OrigArtist,TrackName,OrigTrack = csvread()
	DataDF = DataInit(data,Artist,OrigTrack,TrackName,OrigArtist)	

	PlotData(DataDF)

if __name__ == '__main__':
	main()


		
