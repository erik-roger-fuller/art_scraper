import scrapy
from artscraper.items import Hyperallergic_Dir_Item
from scrapy.loader import ItemLoader
import time
from scrapy.spiders import SitemapSpider


class JustArtnewsSpider(SitemapSpider):
    name = 'just_artnews'
    #allowed_domains
    sitemap_urls = ['https://www.artnews.com/sitemap_index.xml']
    #= ['https://www.artnews.com/post-sitemap202106.xml']

    sitemap_follow = ['/post-sitemap2017','/post-sitemap2016','/post-sitemap2015','/post-sitemap2014',
                      '/post-sitemap2013','/post-sitemap2012','/post-sitemap2011','/post-sitemap2010',
                      '/post-sitemap200', '/post-sitemap19']

    #def sitemap_filter(self, entries):
    #   for entry in entries:
    #        test = entry['loc'].split("/")
    #        test = test[3]
    #        try:
    #            if test[:12] == "post-sitemap":
    #                print(entry)
    #                yield entry
    #        except IndexError:
    #            pass

    def parse(self, response):
        item = Hyperallergic_Dir_Item
        l = ItemLoader(item=Hyperallergic_Dir_Item(), response=response)

        l.add_xpath("title" , '//meta[@property="og:title"]/@content')
        l.add_xpath("para", '//p[@class="p1"]/descendant-or-self::text()|//p[@class="p2"]/descendant-or-self::text()'
                            '|//span[@class="s1"]/descendant-or-self::text()|//span[@class="s2"]/descendant-or-self::text()'
                            '|//div[contains(@class,"a-content")]/p/descendant-or-self::text()')

        l.add_xpath("captions", '//div[@class="post-content-image // "]/figure/div/div/img/@alt')
        l.add_xpath("images", '//div[@class="post-content-image // "]/figure/div/div/img/@data-lazy-src')

        l.add_xpath("author", '//meta[@name="author"]/@content')

        l.add_xpath("pubtime", '//meta[@property="article:published_time"]/@content')
        l.add_xpath("tag", '//meta[@name="news_keywords"]/@content|//meta[@name="keywords"]/@content')

        url = response.url
        l.add_value('url', url)
        test = url.split('/')
        if test[3] == 'art-in-america':
            l.add_value('source', "Art in America")
            #print(test[3], "===art-in-america!!!!")
        else:
            l.add_value('source', 'ARTNews')
            #print(test[3])

        yield l.load_item()