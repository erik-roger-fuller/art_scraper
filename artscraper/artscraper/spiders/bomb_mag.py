import scrapy
from artscraper.items import Artag_and_eflux_Item
from scrapy.loader import ItemLoader
import time
from scrapy.spiders import SitemapSpider


class BombMagSpider(SitemapSpider):
    name = 'bomb_mag'
    sitemap_urls = ['https://www.bombmagazine.org/sitemap.xml']
    #start_urls = ['http://https://www.bombmagazine.org/sitemap.xml/']

    sitemap_follow = ['/sitemap_sections_3_1']

    def parse(self, response):
        item = Artag_and_eflux_Item
        l = ItemLoader(item=Artag_and_eflux_Item(), response=response)

        l.add_xpath("title", '//h1[contains(@class,"title")]/descendant-or-self::text()') #!

        l.add_xpath("para", '//div[contains(@class,"textblock")]/descendant-or-self::text()'
                            '|//div[contains(@class,"abstract")]/descendant-or-self::text()') #!

        l.add_xpath("captions", '//div[contains(@class,"picture")]/img/@alt')#!
        l.add_xpath("images", '//div[contains(@class,"picture")]/img/@data-src')#!

        l.add_xpath("author", '//h1[contains(@class,"title")]/a/descendant-or-self::text()')#!

        l.add_xpath("pubtime", '//time/@datetime')#!

        l.add_xpath("tag", '//ul[contains(@class,"entry--categories")]/li/descendant-or-self::text()')#!

        l.add_value('url', response.url)

        l.add_value('source', "BOMB mag")

        yield l.load_item()