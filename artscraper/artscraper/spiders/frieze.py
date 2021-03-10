import scrapy
from scrapy.spiders import SitemapSpider
from artscraper.items import Frieze_Item
from scrapy.loader import ItemLoader

class FriezeSpider(SitemapSpider):
    name = 'frieze'
    #allowed_domains = ['https://www.frieze.com/sitemap.xml']
    sitemap_urls = ['https://www.frieze.com/sitemap.xml?page=1',
                    'https://www.frieze.com/sitemap.xml?page=2',
                    'https://www.frieze.com/sitemap.xml?page=3',
                    'https://www.frieze.com/sitemap.xml?page=4',
                    'https://www.frieze.com/sitemap.xml?page=5',

                    'https://www.frieze.com/sitemap.xml?page=6',
                    'https://www.frieze.com/sitemap.xml?page=7',
                    'https://www.frieze.com/sitemap.xml?page=8']

    def parse(self, response):
        item = Frieze_Item
        l = ItemLoader(item=Frieze_Item(), response=response)

        l.add_xpath('title', '//meta[@property="og:title"]/@content')

        l.add_xpath('para', '//span[@class="body-text"]/*/text()'
                            '|//p/*/text()'
                            '|//span[@class="body-text"]/div/p/text()')

        l.add_xpath('images', '//figure/img/@src')

        l.add_xpath('captions', '//figcaption/text()')
                                #'|//div[contains(@class,"caption")]/'
                                #'|//p[contains(@class,"caption")]/descendant-or-self::text()')  #

        l.add_xpath('url', '//meta[@property="og:url"]/@content')

        l.add_xpath('author', '//div[@class="node-content-body-author-name"]/a/text()')

        top = response.xpath('//div[@class="article-header-author-info"]/text()').getall()
        try:
            pubtime = top[-1]
            pubtime = pubtime.replace("\n", "")
            pubtime = pubtime.strip()
            pubtime = pubtime.replace("  ", "")
            pubtime = pubtime.replace("|", "")
            l.add_value('pubtime', pubtime)
        except IndexError:
            pass



        l.add_xpath('tag', '//a[contains(@href,"tags")]/descendant-or-self::text()')

        l.add_value('source', 'Frieze')

        yield l.load_item()

"""
'https://www.frieze.com/sitemap.xml?page=9',
'https://www.frieze.com/sitemap.xml?page=10',

'https://www.frieze.com/sitemap.xml?page=11',
'https://www.frieze.com/sitemap.xml?page=12',
'https://www.frieze.com/sitemap.xml?page=13',
'https://www.frieze.com/sitemap.xml?page=14'
"""