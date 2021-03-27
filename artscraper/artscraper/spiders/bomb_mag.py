import scrapy


class BombMagSpider(scrapy.Spider):
    name = 'bomb_mag'
    allowed_domains = ['https://www.bombmagazine.org/sitemap.xml']
    start_urls = ['http://https://www.bombmagazine.org/sitemap.xml/']

    def parse(self, response):
        pass
