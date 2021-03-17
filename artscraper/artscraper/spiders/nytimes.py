import scrapy
from artscraper.items import Nytimes_Dir_Item
from scrapy.loader import ItemLoader
import time
import os
from scrapy.spiders import SitemapSpider
import csv


class NytimesSpider(scrapy.Spider):
    name = 'nytimes'
    #allowed_domains = ['https://www.nytimes.com/sitemap/']
    #start_urls = ['http://https://www.nytimes.com/sitemap//']

    def start_requests(self):
        filename = f"Nytimes_arts_final_arts_links_2000_2021.csv"
        filepath = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art', filename)

        urls = []

        with open(filepath, newline='') as csvfile:
            read_csv = csv.reader(csvfile, delimiter=",")
            for row in read_csv:
                link_dump = row[1]
                link_dump = link_dump.replace("[", "").replace("]", "").replace("'", "")
                # print(link_dump)
                # link_dump = (', '.join(row))
                links = link_dump.split(", ")
                # print(links)
                for link in links:
                    link = link.replace(" ", "")
                    if link == "":
                        pass
                    else:
                        # print(link)
                        urls.append(link)

        #urls.reverse()
        #print(urls)
        print(len(urls))
        badurls =[]

        for url in urls[333:400]: #[111102:111115]:
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
        item = Nytimes_Dir_Item
        l = ItemLoader(item=Nytimes_Dir_Item(), response=response)


        l.add_xpath('title', '//meta[@property="og:title"]/@content')

        l.add_xpath('para', '//section[@name="articleBody"]/*/*/p/text()|'
                            '//section[@name="articleBody"]/*/*/*/a/text()|'
                            '//blockquote/*/text()') #set

        l.add_xpath('captions', "//figcaption/*/text()|"
                                "//picture/img/@alt")

        l.add_xpath('images', '//picture/img/@src')

        l.add_xpath('author', '//span[@itemprop="name"]/a/text()' )

        l.add_xpath('url', '//meta[@property="og:url"]/@content')


        l.add_xpath('pubtime', '//time/@datetime')

        l.add_xpath('tag', '//meta[@property="article:tag"]/@content')

        l.add_value('source', 'Nytimes_Arts')

        yield l.load_item()

#//picture/img
"""        image_dir = response.xpath('//picture/img/@src').getall()
        images = []
        for repo in image_dir:
            repos = str(repo)
            repos = repos[2:]
            fullrepo = ("https://www." + repos)
            images.append(fullrepo)"""