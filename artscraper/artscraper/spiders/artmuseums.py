import scrapy
#from artscraper.items import Juxtapoz_Item
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
import os

class ArtmuseumsSpider(scrapy.Spider):
    name = 'artmuseums'
    allowed_domains = []
    start_urls = [']




    def parse(self, response):
        pass
