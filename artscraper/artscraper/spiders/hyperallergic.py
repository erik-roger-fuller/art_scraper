import scrapy

class HyperallergicSpider(scrapy.Spider):
    name = "hyperallergic"
    start_urls = ['https://hyperallergic.com/']

    def parse(self, response):
        links = response.xpath("//amp-img/@src")
        html = ""

        for link in links:
            url = link.get()

            if any(extension in url for extension in
                   [".jpg" , ".gif" , ".png"]):
                html += """<a href="{url}"
                target="_blank:>
                <img src="{url} height = "100%"
                width="100%"/>
                <a/>""".format(url=url)

                with open ("ha_frontpage.html", "a") as page:
                    page.write(html)
                    page.close()
