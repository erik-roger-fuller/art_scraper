import scrapy
from artscraper.items import Hyperallergic_Dir_Item
from scrapy.loader import ItemLoader
import time
from scrapy.spiders import SitemapSpider
import json


class HyperaldirSpider(SitemapSpider):
    name = 'hyperaldir'
    #allowed_domains = ['https://hyperallergic.com/wp-sitemap-posts-post-1.xml']
    sitemap_urls = ['https://hyperallergic.com/wp-sitemap-posts-post-15.xml/']


    def parse(self, response):
        item = Hyperallergic_Dir_Item

        #allpage = self  #response.css('body')

        pubtime = response.xpath('//meta[@property="article:published_time"]/@content').get()
        #print(pubtime)
        ye, mo, da = int(pubtime[:4]), int(pubtime[5:7]),int(pubtime[8:10])
        print(ye,mo,da)
        if ye == 2021 and mo > 2:
            l = ItemLoader(item=Hyperallergic_Dir_Item(), response=response)
            l.add_xpath('title', '//meta[@property="og:title"]/@content')
            l.add_xpath('para', '/html/body/div[1]/div[2]/section/main/div/article/'
                                'div[1]/child::p/descendant-or-self::text()'
                                '|//article/div[1]/blockquote/p/descendant-or-self::text()'
                                '|//article/div[1]/ul/li/descendant-or-self::text()'
                                '|//article/div[1]/ol/li/descendant-or-self::text()'
                                '|//article/div[1]/h2/descendant-or-self::text()')
            l.add_css('captions', 'figcaption::text, p.wp-caption-text::text')
            l.add_xpath('images', '//article/div[1]/child::div/amp-img/@src')
            l.add_xpath('author', '//meta[@name="author"]/@content')
            l.add_xpath('pubtime', '//meta[@property="article:published_time"]/@content')
            l.add_xpath('tag', '/html/body/div[1]/div[2]/section/main/div/article/'
                               'footer/span/a/text()')
            l.add_xpath('url', '//meta[@property="og:url"]/@content')
            l.add_value('source', 'Hyperallergic')

            yield l.load_item()

        elif ye == 2021 and mo == 2 and da >= 20:
            l = ItemLoader(item=Hyperallergic_Dir_Item(), response=response)
            l.add_xpath('title', '//meta[@property="og:title"]/@content')
            l.add_xpath('para', '/html/body/div[1]/div[2]/section/main/div/article/'
                                'div[1]/child::p/descendant-or-self::text()'
                                '|//article/div[1]/blockquote/p/descendant-or-self::text()'
                                '|//article/div[1]/ul/li/descendant-or-self::text()'
                                '|//article/div[1]/ol/li/descendant-or-self::text()'
                                '|//article/div[1]/h2/descendant-or-self::text()')
            l.add_css('captions', 'figcaption::text, p.wp-caption-text::text')
            l.add_xpath('images', '//article/div[1]/child::div/amp-img/@src')
            l.add_xpath('author', '//meta[@name="author"]/@content')
            l.add_xpath('pubtime', '//meta[@property="article:published_time"]/@content')
            l.add_xpath('tag', '/html/body/div[1]/div[2]/section/main/div/article/'
                               'footer/span/a/text()')
            l.add_xpath('url', '//meta[@property="og:url"]/@content')
            l.add_value('source', 'Hyperallergic')

            yield l.load_item()

        else:
            pass


"""
,
                    'https://hyperallergic.com/wp-sitemap-posts-post-2.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-3.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-4.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-5.xml/',

                    'https://hyperallergic.com/wp-sitemap-posts-post-6.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-7.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-8.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-9.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-10.xml/',

                    'https://hyperallergic.com/wp-sitemap-posts-post-11.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-12.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-13.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-14.xml/',
                    'https://hyperallergic.com/wp-sitemap-posts-post-15.xml/' ]

"""