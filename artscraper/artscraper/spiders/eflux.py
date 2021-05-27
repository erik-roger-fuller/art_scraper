import scrapy
import scrapy
from artscraper.items import Artforum_Dir_Item
from scrapy.loader import ItemLoader
import time
from scrapy.spiders import SitemapSpider

class EfluxSpider(SitemapSpider):
    name = 'eflux'
    #allowed_domains = ['www.e-flux.com']
    sitemap_urls = ['https://www.e-flux.com/sitemap.xml']

    def sitemap_filter(self, entries):
        for entry in entries:
            test = entry['loc'].split("/")
            try:
                if test[3] == "journal" or "program" and len(test)>6:
                    #https://www.e-flux.com/journal/
                    print(entry)
                    yield entry
            except IndexError:
                pass

    def parse(self, response):
        item = Artforum_Dir_Item
        l = ItemLoader(item=Artforum_Dir_Item(), response=response)

        l.add_xpath('title', '//h1/descendant-or-self::text()') #![@class="article-title"]

        l.add_xpath('para', '//div[contains(@class,"block-text")]/descendant-or-self::text()'
                            '|//div[contains(@class,"body-text")]/descendant-or-self::text()'
                            '|//h2/text()')

        #|//div[@class="article-body-text text-style js-sidebar-min-height"]/descendant-or-self::text()'

        l.add_xpath('captions', '//a[contains(@class,"lightbox")]/@title')

        l.add_xpath('images', '//a[contains(@class,"lightbox")]/@href')

        l.add_xpath('author', '//div[@class="article-authors"]/descendant-or-self::text()')

        l.add_xpath('pubtime', '//div[@class="badge badge-date"]/text()'
                               '|//div[@class="article-head-posted"]/descendant-or-self::text()'
                               '|//div[@class="article-headline"]/descendant-or-self::text()')
        #sidebar-item-eventinfo-text
        url = response.url
        mtag = url.split("/")
        mtag = mtag[3]

        tag = response.xpath("//title/text()").get()
        tag = tag.split(" - ")
        tag = tag[1:]
        tag.append(mtag)

        l.add_value('tag', tag)

        l.add_value('url', response.url)
        l.add_value('source', 'eflux')

        yield l.load_item()


"""
        def sitemap_filter(self, entries):
            for entry in entries:
                ent_time = datetime.strptime(str(entry['lastmod'][:10]), '%Y-%m-%d')
                if ent_time.year == 2021 and ent_time.month > 2:
                    if str(entry['loc'][23:30]) == 'article':
                        # https://www.frieze.com/article/
                        print(entry)
                        yield entry
                elif ent_time.year == 2021 and ent_time.month == 2 and ent_time.day >= 26:
                    if str(entry['loc'][23:30]) == 'article':
                        print(entry)
                        yield entry
                else:
                    pass
                    
"""