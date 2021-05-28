import scrapy


class SothebysSpider(scrapy.Spider):
    name = 'sothebys'
    allowed_domains = ['www.sothebys.com']
    start_urls = ['http://www.sothebys.com/']

    def parse(self, response):
        pass
