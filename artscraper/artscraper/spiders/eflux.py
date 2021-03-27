import scrapy


class EfluxSpider(scrapy.Spider):
    name = 'eflux'
    allowed_domains = ['https://www.e-flux.com/sitemap.xml']
    start_urls = ['http://https://www.e-flux.com/sitemap.xml/']

    def parse(self, response):
        pass
