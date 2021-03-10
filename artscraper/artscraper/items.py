# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
import re


def tags_and_unicode(xxx):
    yyy = remove_tags(xxx)
    zzz = yyy.replace("\xa0", " ")
    aaa = zzz.replace("\n", " ")
    zzz = aaa.replace("  ", " ")
    aaa = zzz.replace("\t", "")
    zzz = aaa.strip()
    aaa = zzz.replace( "© FRIEZE 2020" , "")
    return aaa


class Artnet_Article_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    para = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    title = Field(input_processor=Join(), output_processor=TakeFirst())  #input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    tag = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(input_processor=Join(), output_processor=TakeFirst())
    source = Field()

class Artnet_Frontpage_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field(input_processor = Join(), output_processor = TakeFirst())
    author = Field(input_processor = Join(), output_processor = TakeFirst())
    blurb = Field(input_processor = Join(), output_processor = TakeFirst())
    link = Field(input_processor = Join(), output_processor = TakeFirst())
    thumbn = Field(input_processor = Join(), output_processor = TakeFirst())
    pubtime = Field(input_processor = Join(), output_processor = TakeFirst())


"""hyperallergic"""

class Hyperallergic_Dir_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(output_processor=TakeFirst())
    tag = Field()
    source = Field(output_processor=TakeFirst())

class Artforum_Dir_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(output_processor=TakeFirst())
    tag = Field()
    url = Field()
    source = Field(output_processor=TakeFirst())

class Frieze_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(output_processor=TakeFirst())
    tag = Field()
    url = Field()
    source = Field(output_processor=TakeFirst())


"""   
scrapy crawl artnetarticles
scrapy crawl hyperaldir
scrapy crawl artforum
scrapy crawl frieze
"""