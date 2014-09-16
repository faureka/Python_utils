#!C:/Python27
'''###Countries with Internet When and how much Mobile Access do they have'''

import csv
import ast
import matplotlib.pyplot as plt
from matplotlib import axis,cm
import numpy as np

data = []
with open('CoreIndicators.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		data.append(row)

print data[16]
CountryName = []
Index = []
Year = []
Mobile = []
Internet = []

# for i 