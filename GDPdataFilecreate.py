import pandas as pd
import ast


GDPcapitaData = pd.read_csv('GDPcapita.csv',header = 0)
GDPcapitaData = pd.DataFrame(GDPcapitaData)

CountryName = list(set(GDPcapitaData['Country or Area']))
CountryName = sorted(CountryName)

GDPData = [0] * len(CountryName)
j = 0
for i in xrange(len(GDPcapitaData['Value'])):
	if GDPcapitaData['Year'].iloc[i] == 2010:
			GDPData[j] = GDPcapitaData['AVG Value'].iloc[i]
			j = j+1

GDPcapitaData = pd.DataFrame({'Country' : CountryName,
							'Average GDP Data' : GDPData})

print GDPcapitaData.head()


with open('NewGDPcapita.csv','w+') as fout:
	fout.write('Country' + ',' 'Average GDP Data' + '\n')
	for i in xrange(len(GDPcapitaData['Country'])):
		st = GDPcapitaData['Country'].iloc[i] + ',' + str(GDPcapitaData['Average GDP Data'].iloc[i])
		fout.write(st + '\n' )

