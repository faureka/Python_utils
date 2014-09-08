import re
from os import walk, path


filenames = []
def ifint(s):
	try:
		return int(s)
	except:
		return s

def keygen(s):
	return[ ifint(token) for token in re.split('([0-9]+)',s) ]

def naturalsort(liste):
	liste.sort(key = keygen)
	return liste

def callsort(): 
	naturalsort(filenames)


if __name__ == '__main__':
	with open("dir_info.txt","w+") as fdir:    
		for root,directory,filename in walk("."):
			filenames.extend(filename)
			for dirt in directory:
				fdir.write(dirt + "\n")
	callsort()
	with open("mp3_filenames.txt","w+") as fpoint:
		for names in filenames:
			if path.splitext(names)[1] == '.mp3':
				fpoint.write(names + '\n')
	
		


