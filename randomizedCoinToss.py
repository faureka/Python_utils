import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import shapiro as sp

def two_number():
	a,b= np.random.rand(2)
	return a,b

def gen_norm_num():
	return np.random.normal(0,1)

def choose_num_rand():
	return np.random.randint(0,2)



if __name__ == '__main__':
	storeres = [0]*1000
	for i in xrange(1000):
		tempstore = []
		for _ in xrange(10):
			l = two_number()
			maxab = max(l)
			ind = choose_num_rand()
			choosen = l[ind] 
			normnum = gen_norm_num()
			if normnum > choosen:
				guess = 1									#'larger'
			else:
				guess = 0									#'smaller'
			if maxab == choosen and guess == 1:
				result = 'correct'
			elif maxab != choosen and guess == 0:
				result = 'correct'
			else:
				result = 'incorrect'
			if result == 'correct':
				tempstore.append(1)
			else:
				tempstore.append(0)
		storeres[i] = float(sum(tempstore)) / len(tempstore)	
	print len([f for f in storeres if f > 0.5])
	plt.hist(storeres,bins =10)
	plt.show()
		

