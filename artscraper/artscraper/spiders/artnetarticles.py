import scrapy
from scrapy.loader import ItemLoader

import numpy as np
import pandas as pd
import os
import jsonlines

#from scrapy.spiders import SitemapSpider
from artscraper.items import Artnet_Article_Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ArtnetarticlesSpider(scrapy.Spider):
    name = 'artnetarticles'
    #allowed_domains = ['https://news.artnet.com/' ]
    start_urls = ['https://news.artnet.com/']

    urls = ['https://news.artnet.com/']

    for numb in range(1, 60):
        page = 'http://news.artnet.com/page/'
        url = page + str(numb)
        start_urls.append(url)

    #def start_requests(self):
        # urls_from_page now, not urls from json 'http://news.artnet.com/page/1392'

    def parse(self, response):
        for href in response.css('a.teaser-image::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = Artnet_Article_Item()

        allpage = response.css('body')

        l = ItemLoader(item=Artnet_Article_Item(), selector=allpage)

        bodyl = l.nested_xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
        
        bodyl.add_css('para', 'p:not([class="wp-caption-text"])::text, em::text, strong::text, span::text, p a::text')
        bodyl.add_css('captions' , 'div[class="wp-caption aligncenter"] p::text')
        bodyl.add_css('images' , 'div[class="wp-caption aligncenter"] img::attr(src)' )
        
        metadatal = l.nested_xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]')

        l.add_xpath('title', '//meta[@property="og:title"]/@content')

        l.add_xpath('author', '//meta[@name="sailthru.author"]/@content')

        l.add_xpath('pubtime', '//meta[@property="article:published_time"]/@content')

        l.add_xpath('tag', '//meta[@name="keywords"]/@content')

        #metadatal.add_css('author', "p[class='article-byline'] a::text")
        #metadatal.add_css('pubtime', "p[class='article-byline'] time::attr(datetime)")
        #metadatal.add_css('tag', 'h5::text')

        l.add_xpath('url', '//meta[@property="og:url"]/@content')

        l.add_value('source', 'ArtnetNews')

        yield l.load_item()

"""

        fronturls = []

        for urlno in range(0, 3):  # 1393, 1667):  # 1667):total no
            baseurl = 'http://news.artnet.com/page/'
            finurl = baseurl + str(urlno)
            fronturls.append(finurl)

        for fronturl in fronturls:
            yield scrapy.Request(url=fronturl, callback=self.parse)


        filepath = os.path.join(os.path.expanduser('~'),
                                       'Desktop/scrapy/artscraper/artnetfrontpage2_2021-1_2013.jsonl')
        # link_import = load_jsonl(filepath)
        urls = []
        with jsonlines.open(filepath) as reader:
            for obj in reader:
                #print(obj)
                link = obj.get('link')
                try:
                    link = link[0]
                except TypeError:
                    continue
                link = str(link)
                #print(link)
                urls.append(link)

"""