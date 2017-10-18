import urllib
from bs4 import BeautifulSoup


def getLinks(url):
	l = []

	# Reference - https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python
	urlOpen = urllib.urlopen(url)
	webpage = urlOpen.read()

	# Reference - https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
	soup = BeautifulSoup(webpage, 'html.parser')
	links = soup.find_all('a', href=True)   # a tag in HTML defines the link to new pages

	for a in links:
		if a['href'].startswith('/wiki/'):
			l.append("http://en.wikipedia.org"+a['href'])
	return l

# url = "https://en.wikipedia.org/wiki/Barack_Obama"
# l = getLinks(url)
# print l[100]