import urllib
from bs4 import BeautifulSoup


class UrlReader:
    def __init__(self):
        None

    @staticmethod
    def get_content(url):
        url_open = urllib.urlopen(url)
        return url_open.read()

    @staticmethod
    def parse_content(content):
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a', href=True)  # a tag in HTML defines the link to new pages

        urls = []
        placeholders = ['#', '?']

        for a in links:
            if a['href'].startswith('/wiki/'):
                x = a['href'].split(placeholders[0])  # Remove placeholders
                x = x[0].split(placeholders[1])  # Remove placeholders
                urls.append("http://en.wikipedia.org" + x[0])
        return urls
