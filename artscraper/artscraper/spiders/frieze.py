import scrapy
from scrapy.spiders import SitemapSpider
from artscraper.items import Frieze_Item
from scrapy.loader import ItemLoader
from datetime import datetime

def frieze_time_to_df(line):
    line = "".join(line)
    line = line.replace("	", "").replace("\n", ' ')
    line = line.replace("\r", " ")
    pubtime_i = line.strip()
    pubtime_i = pubtime_i.title()
    pubtime = datetime.strptime(pubtime_i, "%d %b %y")
    return pubtime
    # frieze : "pubtime": "31 OCT 18"

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

    def sitemap_filter(self, entries):
        for entry in entries:
            ent_time = datetime.strptime(str(entry['lastmod'][:10]), '%Y-%m-%d')
            if ent_time.year == 2021 and ent_time.month > 2:
                if str(entry['loc'][23:30]) == 'article':
                    #https://www.frieze.com/article/
                    print(entry)
                    yield entry
            elif ent_time.year == 2021 and ent_time.month == 2 and ent_time.day >= 26:
                if str(entry['loc'][23:30]) == 'article':
                    print(entry)
                    yield entry
            else:
                pass

    def parse(self, response):
        top = response.xpath('//div[@class="article-header-author-info"]/text()').getall()
        try:
            pubtime = top[-1]
            pubtime = pubtime.replace("\n", "")
            pubtime = pubtime.strip()
            pubtime = pubtime.replace("  ", "")
            pubtime = pubtime.replace("|", "")
            pubtime = frieze_time_to_df(pubtime)
            if pubtime.year == 2021 and pubtime.month > 2:
                item = Frieze_Item
                l = ItemLoader(item=Frieze_Item(), response=response)
                l.add_xpath('title', '//meta[@property="og:title"]/@content')
                l.add_xpath('para', '//span[@class="body-text"]/*/text()'
                                    '|//p/*/text()'
                                    '|//span[@class="body-text"]/div/p/text()'
                                    '|//span[@class="body-text"]/descendant-or-self::*/text()')
                l.add_xpath('images', '//figure/img/@src')
                l.add_xpath('captions', '//figcaption/text()')
                l.add_xpath('url', '//meta[@property="og:url"]/@content')
                l.add_xpath('author', '//div[@class="node-content-body-author-name"]/a/text()')
                l.add_xpath('tag', '//a[contains(@href,"tags")]/descendant-or-self::text()')
                pubtime = datetime.strftime(pubtime, "%Y-%m-%d")
                l.add_value('pubtime', pubtime)
                l.add_value('source', 'Frieze')
                yield l.load_item()
            elif pubtime.year == 2021 and pubtime.month == 2 and pubtime.day >= 26:
                item = Frieze_Item
                l = ItemLoader(item=Frieze_Item(), response=response)
                l.add_xpath('title', '//meta[@property="og:title"]/@content')
                l.add_xpath('para', '//span[@class="body-text"]/*/text()'
                                    '|//p/*/text()'
                                    '|//span[@class="body-text"]/div/p/text()'
                                    '|//span[@class="body-text"]/descendant-or-self::*/text()')
                l.add_xpath('images', '//figure/img/@src')
                l.add_xpath('captions', '//figcaption/text()')
                l.add_xpath('url', '//meta[@property="og:url"]/@content')
                l.add_xpath('author', '//div[@class="node-content-body-author-name"]/a/text()')
                l.add_xpath('tag', '//a[contains(@href,"tags")]/descendant-or-self::text()')
                pubtime = datetime.strftime(pubtime, "%Y-%m-%d")
                l.add_value('pubtime', pubtime)
                l.add_value('source', 'Frieze')
                yield l.load_item()
        except IndexError:
            pass
