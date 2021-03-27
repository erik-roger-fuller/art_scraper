import scrapy
from scrapy.spiders import SitemapSpider
from artscraper.items import Juxtapoz_Item
from scrapy.loader import ItemLoader


class Juxtapoz_Spider(SitemapSpider):
    name = 'juxtapoz'
    #allowed_domains = ['https://www.juxtapoz.com/']
    map = 'https://www.juxtapoz.com/index.php?option=com_jmap&view=sitemap&format=xml'
    sitemap_urls = []

    def parse(self, response):
        item = Frieze_Item
        l = ItemLoader(item=Juxtapoz_Item(), response=response)

        """no modifi3ed tabs yet"""

        l.add_xpath('title', '//meta[@property="og:title"]/@content')

        l.add_xpath('para', '//span[@class="body-text"]/*/text()'
                            '|//p/*/text()'
                            '|//span[@class="body-text"]/div/p/text()')

        l.add_xpath('images', '//figure/img/@src')

        l.add_xpath('captions', '//figcaption/text()')

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

        l.add_value('source', 'Juxtapoz')

        yield l.load_item()
