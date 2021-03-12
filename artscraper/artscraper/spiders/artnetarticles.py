import scrapy
from scrapy.loader import ItemLoader

import numpy as np
import pandas as pd
import os
import jsonlines

from artscraper.items import Artnet_Article_Item

class ArtnetarticlesSpider(scrapy.Spider):
    name = 'artnetarticles'
    #allowed_domains = ['https://news.artnet.com/' ]
    #start_urls = ['http://https://news.artnet.com/']

    def start_requests(self):
        # urls_from_json
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

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Artnet_Article_Item()

        allpage = response.css('body')

        l = ItemLoader(item=Artnet_Article_Item(), selector=allpage)

        bodyl = l.nested_xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
        
        bodyl.add_css('para', 'p:not([class*="wp-caption-text"])::text, em::text, strong::text, span::text, p a::text')
        bodyl.add_css('captions' , 'div[class="wp-caption aligncenter"] p::text')
        bodyl.add_css('images' , 'div[class="wp-caption aligncenter"] img::attr(src)' )
        
        metadatal = l.nested_xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]')

        metadatal.add_css('title', 'h1::text')
        metadatal.add_css('author', "p[class='article-byline'] a::text")
        metadatal.add_css('pubtime', "p[class='article-byline'] time::attr(datetime)")
        metadatal.add_css('tag', 'h5::text')

        l.add_value('source', 'ArtnetNews')

        yield l.load_item()
