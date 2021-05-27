import scrapy
#from artscraper.items import Museum_Item
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
import os

class ArtmuseumsSpider(scrapy.Spider):
    name = 'artmuseums'
    allowed_domains = []
    start_urls = ['']


    def start_requests(self):
        filename1 = 'barnes_sitemap.xml'
        #filepath1 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art/art_writing/juxtapoz', filename1)

        urls = []
        with open(filename1, 'r') as read_path:
            soup = BeautifulSoup(read_path, 'xml')
            linx = soup.select('loc')
            for link in linx:
                link = link.get_text()
                #print(link)
                if link[-7:] == "details":
                    urls.append(link)
                else:
                    pass
        #urls = urls[:-22]
        #print(urls)
        print(len(urls))
        badurls =[]

        for url in urls[1110:1120]: #[111102:111115]:
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
        #item = Museum_Item
        l = ItemLoader(item=Museum_Item(), response=response)

        title = response.xpath('//meta[@name="title"]/@content').get()
        title = title.split(":")
        l.add_value("title", title[1])

        l.add_value("artist", (title[0].replace( "Barnes Collection Online — " , "")))
        #l.add_xpath('title', '//meta[@name="title"]/@content')  ###

        l.add_xpath('images', '//div[class="image-art-object"]/img')  ###[@/@src

        #l.add_xpath('author', '//div[@class="table-row"]/@content')  # ?#

        #l.add_xpath('author', '//div[@class="table-row"]/@content')div[@class="image-caption"]/div/text()
        l.add_xpath('captions', '///html/body/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[3]/div')  ###og:description
        #"/html/body/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[1]/img"
        l.add_xpath('url', '//meta[@property="og:url"]/@content')  ###

        l.add_value('source', 'Barnes')  ###

        yield l.load_item()

"""
Location
On View: Room 13, East Wall
Artist
Vincent van Gogh (Dutch, 1853 - 1890)
Year
January–March 1887
Medium
Oil on canvas
Accession Number
BF720
Dimensions
Overall (oval): 23 1/2 x 29 in. (59.7 x 73.7 cm)
"""