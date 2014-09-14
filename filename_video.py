import urllib

d = 0
with open ("filename_video.txt",'r') as f:
	 for d in f:
#	 	d = f.read()
		k = d.zfill(4).strip()
		url = 'http://nitin.ee.igloonet/5134/lectures/video/%s.avi' %k
		filename_use = "%s.avi" %k 
		urllib.urlretrieve(url,filename_use)
		d = 0
