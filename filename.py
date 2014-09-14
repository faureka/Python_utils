import urllib
d = 0
with open ("filename.txt",'r') as f:
	 for d in f:
#	 	d = f.read()
		k = d.zfill(4).strip()
		url = 'http://nitin.ee.igloonet/5134/lectures/notes/%s.pdf' %k
		filename_use = "%s.pdf" %k 
		urllib.urlretrieve(url,filename_use)
		d = 0
#f.close()		
