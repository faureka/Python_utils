import random 
from collections import OrderedDict
import plistlib as pl
import csv
from datetime import datetime
# from csvmodule import *

XMLread = []
dateToday = datetime.today()
WeightDict = {}
DictOrdered = OrderedDict()


def readITunesXML():
	count = 0
	xml = 'C:\Users\stifler\Downloads\study material\OCW\UN data Analysis\Python_utils\iTunes Music Library.xml'
	XMLdata = pl.readPlist(xml)
	trackID = XMLdata['Tracks'].keys()
	print trackID[0:10]
	with open('Itunes.csv','w+') as fout:
	# csv.writer(fout,head)
		for trackid in trackID: 
			# line = [str(data['Tracks'][trackid]['Artist']) , str(data['Tracks'][trackid]['Name']),str(data['Tracks'][trackid]['Play Count']),str(data['Tracks'][trackid]['Total Time']]
			try:
				fout.write(str(XMLdata['Tracks'][trackid]['Name'])+','+str(XMLdata['Tracks'][trackid]['Play Count'])+
					','+str(XMLdata['Tracks'][trackid]['Date Added'])+','+str(XMLdata['Tracks'][trackid]['Play Date UTC'])+','+str(XMLdata['Tracks'][trackid]['Rating'])+'\n')
			except Exception , e:
				count = count + 1
		print count		
	fout.close()

def csvreader():
	# if os.path.isfile("main\BillDetails.csv"):
	with open("Itunes.csv","r") as fcsv:
		fhandle = csv.reader(fcsv,delimiter = ",")
		for row in fhandle:
			XMLread.append(row)
	# print XMLread[2]		
	fcsv.close()
	

def dateformat():
	for i in xrange(len(XMLread)):
		XMLread[i][2] = datetime.strptime(XMLread[i][2],"%d-%m-%y %H:%M").strftime("%d-%m-%y")
		XMLread[i][3] = datetime.strptime(XMLread[i][3],"%d-%m-%y %H:%M").strftime("%d-%m-%y")
		XMLread[i].append((dateToday - datetime.strptime(XMLread[i][2],"%d-%m-%y")).days)						
		XMLread[i].append((dateToday - datetime.strptime(XMLread[i][3],"%d-%m-%y")).days)						

def dictCreator():
	for i in xrange(len(XMLread)):
		WeightDict[XMLread[i][0]] = XMLread[i][7]

def WeightCreator(WeightedVal):
	''' Last Played Weightage'''
	for i in xrange(len(XMLread)):
		
		tempLP = XMLread[i][6]
		if 0 <= tempLP <= 10:
			WeightedVal[i].append(5)
		elif 11 <=tempLP<=20:
			WeightedVal[i].append(4)
		elif 21 <=tempLP<=25:
			WeightedVal[i].append(3)
		elif 25 < tempLP<=28:
			WeightedVal[i].append(2)
		elif 28 <tempLP<=31:
			WeightedVal[i].append(1)
		else:
			WeightedVal[i].append(0.5)
		
		tempADD = XMLread[i][5]	
		if 0 <= tempLP <= 7:
			WeightedVal[i].append(5)
		elif 8 <=tempLP<=14:
			WeightedVal[i].append(4)
		elif 15 <=tempLP<=30:
			WeightedVal[i].append(3)
		elif 30 < tempLP<=180:
			WeightedVal[i].append(2)
		elif 180 <tempLP:
			WeightedVal[i].append(1)
		
		tempPlayed = XMLread[i][1]
		if 10 < tempPlayed < 40:
			WeightedVal[i].append(3)
		elif 60 <tempLP:
			WeightedVal[i].append(4)
		elif 0 <=tempLP<=10:
			WeightedVal[i].append(2)	
		elif 40<=tempLP<=60:
			WeightedVal[i].append(5)

	return WeightedVal		

def Weights(WeightedVal):
	for i in xrange(len(XMLread)):
		tempVal = int(XMLread[i][4])*0.1 + WeightedVal[i][2]*0.3 + WeightedVal[i][1]*0.15 + WeightedVal[i][0]*0.05
		XMLread[i].append(tempVal)

def fileWriter(Dictkeys):
	with open("playlist.txt","w+") as ftxt:
		for songs in Dictkeys:
			ftxt.write(str(songs) + "\n")
	ftxt.close()
			

def main():
	# readITunesXML()
	csvreader()
	dateformat()
	WeightedVal = [[] for i in xrange(len(XMLread))]
	WeightedVal = WeightCreator(WeightedVal)
	Weights(WeightedVal)
	dictCreator()
	DictOrdered = OrderedDict(sorted(WeightDict.items(),key=lambda t:random.random()*t[1], reverse = True))
	fileWriter(DictOrdered.keys())

	# print XMLread[2]
	# print WeightedVal[1] , XMLread[1]
	# fhandle = csvwriter()
	# fhandle.csvwrite(DictOrdered.keys())
	# print XMLread[2]
	# print "%s" %(dateToday - datetime.strptime(XMLread[2][2],"%d-%m-%y")).days
	# print WeightDict.keys()

if __name__ == '__main__':
	main()

