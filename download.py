import urllib
import urllib2

codes = open("gag.txt", "r")

def download():
	i = 1
	for url in iter(codes):
		name = str(i)+".jpg"
		urllib.urlretrieve(url, name)
		print "finished downloading "+url+"\n"
		i = i + 1

download()