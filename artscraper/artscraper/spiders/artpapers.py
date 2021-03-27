import scrapy


class ArtpapersSpider(scrapy.Spider):
    name = 'artpapers'
    allowed_domains = ['https://www.artpapers.org/sitemap_index.xml']
    start_urls = ['http://https://www.artpapers.org/sitemap_index.xml/']

    def parse(self, response):
        pass
