import scrapy
from scrapy.loader import ItemLoader
from artscraper.items import Artag_and_eflux_Item


class ArtagendaSpider(scrapy.Spider):
    name = 'artagenda'
    allowed_domains = ['www.art-agenda.com']
    start_urls = ['http://www.art-agenda.com/']

    for year in range(2004, 2021):
        page = 'http://www.art-agenda.com/'
        url1 = f"{page}/announcements/{str(year)}/"
        start_urls.append(url1)
        url2 = f"{page}/features/{str(year)}/"
        start_urls.append(url2)

        # def start_requests(self):
        # urls_from_page now, not urls from json 'http://news.artnet.com/page/1392'panel-column-right-

    def parse(self, response):
        for href in response.xpath('//a[@class="read-more"]/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = Artag_and_eflux_Item
        l = ItemLoader(item=Artag_and_eflux_Item(), response=response)

        l.add_xpath('title', '//title/text()')  # '//h1/descendant-or-self::text()'

        doubletake = response.xpath('//div[contains(@class,"dubletake-text")]')
        if len(doubletake) != 0:
            l.add_xpath('para', '//div[contains(@class,"dubletake-text")]/descendant-or-self::text()')
        else:
            l.add_xpath('para', '//div[contains(@class,"body-text")]/descendant-or-self::text()')

        # |//div[@class="article-body-text text-style js-sidebar-min-height"]/descendant-or-self::text()'

        l.add_xpath('captions', '//div[contains(@class,"item-image")]/img/@data-caption')

        l.add_xpath('images', '//div[contains(@class,"item-image")]/img/@src'
                              '|//a[contains(@class,"lightbox")]/@href')

        l.add_xpath('author', '//div[@class="article-author"]/p/strong/descendant-or-self::text()')#'//div[@class="article-authors"]/descendant-or-self::text()')

        #l.add_xpath('pubtime',

        pubtime = response.xpath( '//div[@class="badge badge-date"]/text()'
                               '|//div[@class="article-head-posted"]/descendant-or-self::text()').getall()

        pubtime = "".join(pubtime)
        pubtime = str(pubtime)
        l.add_value("pubtime", pubtime)

        url = response.url
        mtag = url.split("/")
        mtag = mtag[3]

        tag = response.xpath('//div[@class="article-head-client"]/a/text()').getall()
        tag.append(mtag)

        l.add_value('tag', tag)

        l.add_value('url', url)
        l.add_value('source', 'artagenda')

        yield l.load_item()
