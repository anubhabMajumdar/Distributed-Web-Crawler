# Reference - https://stackoverflow.com/questions/18903197/scrapy-xpath-all-the-links-on-the-page 
# Accessed on 09/23/2017
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field


class MyItem(Item):
    url= Field()


class MySpider(CrawlSpider):
    name = 'wikipedia.org'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Barack_Obama']

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=True), )
    
    def parse_url(self, response):
        item = MyItem()
        item['url'] = response.url
        return item

# Reference Ends 

