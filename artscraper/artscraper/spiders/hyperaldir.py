import scrapy
from artscraper.items import Hyperallergic_Dir_Item
from scrapy.loader import ItemLoader
import time
from scrapy.spiders import SitemapSpider
import json


class HyperaldirSpider(SitemapSpider):
    name = 'hyperaldir'
    #allowed_domains = ['https://hyperallergic.com/wp-sitemap-posts-post-1.xml']
    sitemap_urls = ['https://hyperallergic.com/wp-sitemap-posts-post-1.xml/',
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

    def parse(self, response):
        item = Hyperallergic_Dir_Item

        #allpage = self  #response.css('body')

        l = ItemLoader(item = Hyperallergic_Dir_Item(), response=response)

        l.add_xpath('title', '/html/body/div[1]/div[2]/section/main/header/'
                             'child::h1//descendant-or-self::text()')

        l.add_xpath('para', '/html/body/div[1]/div[2]/section/main/div/article/'
                            'div[1]/child::p/descendant-or-self::text()'
                            '|//article/div[1]/blockquote/p/descendant-or-self::text()'
                            '|//article/div[1]/ul/li/descendant-or-self::text()'
                            '|//article/div[1]/ol/li/descendant-or-self::text()'
                            '|//article/div[1]/h2/descendant-or-self::text()')

        l.add_css('captions', 'figcaption::text, p.wp-caption-text::text')

        l.add_xpath('images', '//article/div[1]/child::div/amp-img/@src')

        l.add_xpath('author', '/html/body/div[1]/div[2]/section/main/header/div/'
                              'div[1]/span[2]/span[2]/descendant-or-self::text()')

        l.add_css('pubtime', "span[class='posted-on'] time::attr(datetime)")

        l.add_xpath('tag', '/html/body/div[1]/div[2]/section/main/div/article/'
                           'footer/span/a/text()')

        l.add_value('source', 'Hyperallergic')

        yield l.load_item()


