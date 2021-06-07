import scrapy
from artscraper.items import Hyperallergic_Dir_Item
from scrapy.loader import ItemLoader
import time
from scrapy.spiders import SitemapSpider


class JustArtnewsSpider(SitemapSpider):
    name = 'just_artnews'
    #allowed_domains = ['https://www.artnews.com/sitemap_index.xml']
    sitemap_urls = ['https://www.artnews.com/post-sitemap202106.xml']

    def parse(self, response):
        item = Hyperallergic_Dir_Item
        l = ItemLoader(item=Hyperallergic_Dir_Item(), response=response)

        l.add_xpath("title" , '//meta[@property="og:title"]/@content')
        l.add_xpath("para", '//p[@class="p1"]/descendant-or-self::text()|//p[@class="p2"]/descendant-or-self::text()')

        captions = ("captions", '//div[@class="post-content-image // "]/figure/div/div/img/@alt')
        l.add_xpath("images", '//div[@class="post-content-image // "]/figure/div/div/img/@data-lazy-src')

        l.add_xpath("author", '//meta[@name="author"]/@content')

        l.add_xpath("pubtime", '//meta[@property="article:published_time"]/@content')
        l.add_xpath("tag", '//meta[@name="news_keywords"]/@content|//meta[@name="keywords"]/@content')

        url = response.url
        l.add_value('url', url)
        l.add_value('source', 'ARTNews')

        yield l.load_item()