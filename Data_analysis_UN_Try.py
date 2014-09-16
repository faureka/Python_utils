#!C:/Python27

import csv
import ast
import matplotlib.pyplot as plt
# plt.close('all')
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

data = []
with open('Telecommdata_radio.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		data.append(row)
header = data[0]
# print len(data)
CountryName = []
Index = []
RadioData = []
Year = []
for i in xrange(1,219):
	CountryName.append(str(data[i][1]))
	Index.append(int(data[i][0]))
	if(data[i][2] != '...'):
		RadioData.append(ast.literal_eval(data[i][2]))
	else:	
		RadioData.append(0.0)
print Index[1],RadioData[1]
fig,ax = plt.subplots()
ax.set_xlabel('Country Index')
ax.set_ylabel('Radio in Household(Zeros for data not present)')
ax.set_title('Radio Data from 2008-2012')
ax.bar(Index,RadioData,0.15,color='r')
# ax.set_xticks(range(len(RadioData)))
# ax.set_xticklabels()
# plt.xticks(range(len(Index)),CountryName,size= 'small')
plt.show()
# plt.close()