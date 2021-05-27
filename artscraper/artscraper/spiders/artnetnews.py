import scrapy
import artscraper
import csv
#
from artscraper.items import Artnet_Frontpage_Item
from scrapy.loader import ItemLoader

class ArtnetNewsSpider(scrapy.Spider):
    name = 'artnetnews'

    def start_requests(self):
        urls = [
            'http://news.artnet.com/page/1392'
        ]

        for allurl in range(0,3):   #1393, 1667):  # 1667):total no
            baseurl = 'http://news.artnet.com/page/'
            finurl = baseurl + str(allurl)
            urls.append(finurl)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Artnet_Frontpage_Item()

        media_list = response.css('li.media')

        for media in media_list:
            l = ItemLoader(item=Artnet_Frontpage_Item(), selector=media)

            l.add_css('title', "div.teaser-info a h2::text")
            l.add_css('author', "p.teaser-byline a::text")
            l.add_css('blurb', "div.teaser-info a p::text")
            l.add_css('link', "a.teaser-image::attr(href)")
            l.add_css('thumbn', "a.teaser-image div.image-wrapper img::attr(src)")
            l.add_css('pubtime', "p.teaser-byline time::attr(datetime)")
            # l.add_value('page', = response.url)

            yield l.load_item()

