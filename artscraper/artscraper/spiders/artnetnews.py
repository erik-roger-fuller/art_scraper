import scrapy
import csv
#
from artscraper.items import Artnet_Frontpage_Item
from scrapy.loader import ItemLoader



class ArtnetNewsSpider(scrapy.Spider):
    name = 'artnetnews'

    def start_requests(self):
        urls = [
            'http://news.artnet.com/page/1392'
        ]

        for allurl in range(0,3):   #1393, 1667):  # 1667):total no
            baseurl = 'http://news.artnet.com/page/'
            finurl = baseurl + str(allurl)
            urls.append(finurl)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Artnet_Frontpage_Item()

        media_list = response.css('li.media')

        for media in media_list:
            l = ItemLoader(item=Artnet_Frontpage_Item(), selector=media)

            l.add_css('title', "div.teaser-info a h2::text")
            l.add_css('author', "p.teaser-byline a::text")
            l.add_css('blurb', "div.teaser-info a p::text")
            l.add_css('link', "a.teaser-image::attr(href)")
            l.add_css('thumbn', "a.teaser-image div.image-wrapper img::attr(src)")
            l.add_css('pubtime', "p.teaser-byline time::attr(datetime)")
            # l.add_value('page', = response.url)

            yield l.load_item()

"""
class ArtnetArticleSpider(scrapy.Spider):
    name = 'artnetarticle'

    # def get_urls_from_json:
    filepath = path = os.path.join(os.path.expanduser('~'),
                                   'Desktop/scrapy/artscraper/artnetfrontpage2_2021-1_2013.jsonl')
    link_import = pd.read_json(filepath)
    links = link_import['links']

    urls = []
    for url in links:
        urls.append(url)

    def start_requests(self, urls):
        urls = urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Artnet_Article_Item()

        media_list = response.css('li.media')


        l = ItemLoader(item=Artnet_Frontpage_Item(), selector=media)

--------------------
#l = ItemLoader(item=Product(), response=response)
        for media in media_list:
            yield {
                'title': media.css("div.teaser-info a h2::text").get() ,
                'blurb': media.css("div.teaser-info a p::text").get() ,
                'link': media.css("a.teaser-image").xpath("@href").get() ,
                'thumb-n' : media.css("a.teaser-image").xpath('./div[1]/img[1]').get() ,
                'page' : response.url
            }
        page = response.url.split("/")[-2]
        #page = str(page)[28:]
        filename = f'artnetnews-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

    #def parse_article_contents(self, response):
        #for sel in media.css("a.teaser-image").xpath("@href")


    def extract_with_css(query):
        return response.css(query).get(default='').strip()


 page = response.url.split("/")[-2]
        #page = str(page)[28:]
        filename = f'artnetnews-csv-{page}.csv'
        with open(filename, 'wb') as f:
            f.write(response.body)

   old yeield statement         yield {
                'title': media.css("div.teaser-info a h2::text").get() ,
                'blurb': media.css("div.teaser-info a p::text").get() ,
                'link': media.css("a.teaser-image").xpath("@href").get() ,
                'thumb-n' : media.css("a.teaser-image").xpath('./div[1]/img[1]').get() ,
                'page' : response.url
            }


def parse_article(self, response):



#artnet titles ---  response.css("div.teaser-info a h2::text").extract()
# artnet blurbs ---  response.css("div.teaser-info a p::text").extract()
# artnet links --- response.css("a.teaser-image").xpath("@href").extract()


class HyperallergicSpider(scrapy.Spider):
    name = "hyperal"
    start_urls = ['https://hyperallergic.com/']

    def parse(self, response):
        links = response.xpath("//img/@src")
        html = ""

        for link in links:
            url = link.get()

            if any(extension in url for extension in
                   [".jpg" , ".gif" , ".png"]):
                html += <a href="{url}"
                target="_blank:>
                <img src="{url} height = "100%"
                width="100%"/>
                <a/>.format(url=url)

                with open ("ha_frontpage.html", "a") as page:
                    page.write(html)
                    page.close()

                next_page = response.css('li.next a::attr(href)').get()
                if next_page is not None:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parse)



class ArtnetNewsSpider(scrapy.Spider):
    name = 'artnetnews'
    allowed_domains = ['news.artnet.com']

    start_urls = ['http://news.artnet.com/']

    #links elector
    links = response.xpath('//a/@href')

    #div selector
    divs = response.xpath('//div')


for quote in response.xpath('//ul[@class="media-list"]').getall():


    #paragraph selector
    paragraphs = response.xpath('//p/')

    def parse(self, response):
        for article in response.css(response.css('li.media'):
            yield {
                'p-title': quote.css('h2.teaser-title h2::text').get(),
                'category': quote.css('h5[@class='teaser-category h5']').get(),
                'author' : quote.xpath(
            '/html/body/section[1]/div[2]/div[4]/div/div[1]/div/ul/li[1]/article/div/p/a'
        ).get() ,
                'link': quote.css('//h2').get(),
            }

//article[@id='tease-1942598']//h5[@class='teaser-category h5']
        article_page_links = response.css('div.teaser-info ')
        yield from response.follow_all(article_page_links_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

"""
