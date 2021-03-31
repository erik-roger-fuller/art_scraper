import scrapy
from artscraper.items import Juxtapoz_Item
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
import os

class Juxtapoz_Spider(scrapy.Spider):
    name = 'juxtapoz'
    #allowed_domains = ['https://www.juxtapoz.com/']
    #map = 'https://www.juxtapoz.com/index.php?option=com_jmap&view=sitemap&format=xml'
    sitemap_urls = []

    def start_requests(self):
        filename1 = 'juxtapoz_sitemap.xml'
        filepath1 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art/art_writing/juxtapoz', filename1)

        urls = []
        with open(filepath1, 'r') as read_path:
            soup = BeautifulSoup(read_path, 'lxml')
            linx = soup.select('loc')
            for link in linx:
                link = link.get_text()
                #print(link)
                if link[25:28] == "tag":
                    pass
                else:
                    urls.append(link)
        urls = urls[:-22]
        #print(urls)
        print(len(urls))
        badurls =[]

        for url in urls[2722:2733]: #[111102:111115]:
            try:
                yield scrapy.Request(url=url, callback=self.parse)
            except ValueError:
                badurls.append(url)
                print("HERE!!!!!" + url)
                pass
            except KeyboardInterrupt:
                print(badurls)
        print("END:     ")
        print(badurls)

    def parse(self, response):
        item = Juxtapoz_Item
        l = ItemLoader(item=Juxtapoz_Item(), response=response)

        l.add_xpath('title', '//meta[@name="title"]/@content') ###

        l.add_xpath('para', '//div[@class="articleBody"]/*/text()'
                            '|//p/*/text()'
                            '|//div[@class="articleBody"]/*/*/text()') ###'|//div[@class="articleBody"]/*/*/text()')

        l.add_xpath('images', '//div/img/@src'
                              '|//p/img/@src'
                              '|//a[@href="#"]/img/@src') ###

        l.add_xpath('captions', '//span[@class="caption"]/text()') ###

        l.add_xpath('author', '//meta[@name="author" or @name="rights"]/@content')#?#

        l.add_xpath('url', '//meta[@property="og:url"]/@content') ###

        l.add_xpath('url', '//meta[@name="keywords"]/@content') ###

        raw_time= response.xpath('//div[contains(@class,"dateAndByline")]/text()').get()
        datetime = raw_time.replace(" | in ", "").replace(",", "")
        l.add_value('pubtime', datetime)
        #l.add_xpath('datetime', '//div[contains(@class,"dateAndByline")]/text()') #?#

        l.add_value('source', 'Juxtapoz') ###

        yield l.load_item()



"""
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
            """