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
        # def get_urls_from_json:
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
        #body = response.xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')

        bodyl.add_css('para', 'p:not([class*="wp-caption-text"])::text, em::text, strong::text, span::text, p a::text')
        bodyl.add_css('captions' , 'div[class="wp-caption aligncenter"] p::text')
        bodyl.add_css('images' , 'div[class="wp-caption aligncenter"] img::attr(src)' )
        #yield bodyl.load_item()

        metadatal = l.nested_xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]')
        #metadata = response.xpath('/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]')

        #l = ItemLoader(item=Artnet_Article_Item(), selector=metadata)

        metadatal.add_css('title', 'h1::text')
        metadatal.add_css('author', "p[class='article-byline'] a::text")
        metadatal.add_css('pubtime', "p[class='article-byline'] time::attr(datetime)")
        metadatal.add_css('tag', 'h5::text')

        l.add_value('source', 'ArtnetNews')

        yield l.load_item()






        #l = ItemLoader(item=Artnet_Frontpage_Item(), selector=media)
"""
with open (filepath, 'r') as link_import:
        data = link_import.read()
        obj = json.loads(data)

        links = obj['links']

    urls = []
    for url in links[5]:
        urls.append(url)       
      
        
def load_jsonl(input_path) -> list:
    
    #Read list of objects from a JSON lines file.
    
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data
        
            links = link_import['title']
        for url in links:
            urls.append(url)    
        """