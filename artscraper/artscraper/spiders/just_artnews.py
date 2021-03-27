import scrapy


class JustArtnewsSpider(scrapy.Spider):
    name = 'just_artnews'
    allowed_domains = ['https://www.artnews.com/sitemap_index.xml']
    start_urls = ['http://https://www.artnews.com/sitemap_index.xml/']

    def parse(self, response):
        pass
