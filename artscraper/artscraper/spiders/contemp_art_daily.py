import scrapy


class ContempArtDailySpider(scrapy.Spider):
    name = 'contemp_art_daily'
    allowed_domains = ['https://contemporaryartdaily.com/wp-sitemap.xml']
    start_urls = ['http://https://contemporaryartdaily.com/wp-sitemap.xml/']

    def parse(self, response):
        pass
