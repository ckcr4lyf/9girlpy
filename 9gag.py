import urllib
import urllib2
from bs4 import BeautifulSoup

i = 0
url = "http://9gag.com/girl";
last = ""
gags = open("gag.txt", "w")

def gag(gagurl):
 global last
 response = urllib2.urlopen(gagurl)
 html = response.read()
 soup = BeautifulSoup(html)
 lel = soup.select('article')
 lol = soup.select('img[class="badge-item-img"]')
 for a in lel:
	last = a['data-entry-id']
 for x in lol:
 	gags.write(x['src'])
 	gags.write("\n")

print "About to start while loop..."
print

while i < 300:
	gag(url)
	url = "http://9gag.com/girl?id="+last
	print "Did " + last + " in round number " + str(i)
	i = i + 1