import scrapy
from artscraper.items import Artnet_Article_Item
from scrapy.loader import ItemLoader
import datetime
import time
from scrapy.spiders import SitemapSpider
import json


class ArtnewspaperSpider(scrapy.Spider):
    name = 'artnewspaper'
    #allowed_domains = ['www.theartnewspaper.com']
    start_urls = ['https://www.theartnewspaper.com/rss.xml']

    def parse(self, response):
        for href in response.xpath('//item/guid/text()'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        json_import = response.xpath('//script[@type="application/ld+json"]/text()').getall()  # json import
        json_import = json_import[0]
        json_import = json_import.strip()

        json_head = json.loads(json_import)

        item = Artnet_Article_Item
        l = ItemLoader(item=Artnet_Article_Item(), response=response)

        l.add_xpath('title', '//meta[@property="og:title"]/@content') #!

        l.add_xpath('para', '//p[@itemprop="text"]/text()') #!

        l.add_xpath('images', '//div[@class="image-comp cb-item"]/descendant-or-self::*/img/@data-src') #!

        l.add_xpath('captions', '//div[@class="image-comp cb-item"]/descendant-or-self::*/img/@alt') #!

        l.add_xpath('url', '//meta[@property="og:url"]/@content') #!

        author = json_head['author']
        l.add_value('author', author)

        keywords = json_head['keywords']
        l.add_value('tag', keywords)

        pubtime = json_head['datePublished']
        l.add_value('pubtime', pubtime)

        l.add_value('source', 'artnewspaper')
        yield l.load_item()

"""
    def sitemap_filter(self, entries):
        for entry in entries:
            link = entry["guid"]
            yield link
        top = response.xpath('//div[@class="article-header-author-info"]/text()').getall()

        pubtime = top[-1]
        pubtime = pubtime.replace("\n", "")
        pubtime = pubtime.strip()
        pubtime = pubtime.replace("  ", "")
        pubtime = pubtime.replace("|", "")
        pubtime = frieze_time_to_df(pubtime)
        if pubtime.year == 2021 and pubtime.month > 2:


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