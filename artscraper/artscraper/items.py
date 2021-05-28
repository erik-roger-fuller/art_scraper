# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from dataclasses import dataclass
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join, Compose
from w3lib.html import remove_tags
import re

from datetime import datetime
import time

def tags_and_unicode(xxx):
    aaa = remove_tags(xxx)
    aaa = aaa.replace("\n", " ").replace("  ", " ").replace("’", "'")
    aaa = aaa.replace("\t", "").replace("\xa0", " ")
    zzz = aaa.strip()
    aaa = zzz.replace( " | Artnet News", "").replace("© FRIEZE 2020 |", "")
    aaa = aaa.replace("© FRIEZE 2021 |", "")
    return aaa

def para_clean(para):
    para = remove_tags(para)
    para = para.replace("\xa0", " ").replace("\n", " ").replace("  ", " ")
    para = "".join(para)
    para = para.replace("	", " ").replace("  ", " ").replace("  ", " ")
    para = para.replace("Follow on Facebook:", '').replace("\n", ' ')
    para = para.replace("\r", " ").replace("\t", "")
    para = re.sub(" © 20[0-9][0-9] e-flux and the author", "", para) #eflux
    para = re.sub('[ ]+', ' ', para)
    para = para.strip()
    return para

def iso_time_to_df(pubtime_i):
    pubtime_i = pubtime_i[:19]
    pubtime = datetime(*time.strptime(pubtime_i, "%Y-%m-%dT%H:%M:%S")[:6])
    return pubtime

def frieze_time_to_df(line):
    line = "".join(line)
    line = line.replace("	", "").replace("\n", ' ')
    line = line.replace("\r", " ")
    pubtime_i = line.strip()
    pubtime_i = pubtime_i.title()
    pubtime = datetime.strptime(pubtime_i, "%d %b %y")
    #pubtime = datetime.strftime(pubtime, "%Y-%m-%d")
    return pubtime
    # frieze : "pubtime": "31 OCT 18"

def word_time_to_df(line):
    #line = str(line)
    line = line.replace("	", "").replace("\n", ' ')
    line = line.replace("\r", " ").replace("\t", "").replace(",", "")
    pubtime_i = line.strip()
    pubtime_i = pubtime_i.title()
    #print(pubtime_i)
    pubtime = datetime.strptime(pubtime_i, "%B %d %Y")
    #pubtime = datetime.strftime(pubtime, "%Y-%m-%d")
    return pubtime
    # eflux = January 12, 2016 : "pubtime":

def elim_dupes(x):
  return list(dict.fromkeys(x))

class Artnet_Article_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = Field(input_processor=Join(),output_processor=MapCompose(tags_and_unicode))  # input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    para = Field(input_processor=Join(), output_processor=MapCompose(para_clean))

    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(input_processor=Join(), output_processor=(iso_time_to_df))
    tag = Field(input_processor=Join(), output_processor=TakeFirst())
    url = Field()
    source = Field(output_processor=TakeFirst())


"""hyperallergic"""

class Hyperallergic_Dir_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(para_clean))

    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(input_processor=MapCompose(iso_time_to_df), output_processor=TakeFirst())
    tag = Field()
    url = Field()
    source = Field(output_processor=TakeFirst())

class Artforum_Dir_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(para_clean))
    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field( output_processor=TakeFirst())
    tag = Field()
    url = Field()
    source = Field(output_processor=TakeFirst())


class Artag_and_eflux_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(para_clean))
    captions = Field(input_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(input_processor=MapCompose(word_time_to_df), output_processor=TakeFirst())
    tag = Field()
    url = Field()
    source = Field(output_processor=TakeFirst())

class Nytimes_Dir_Item(scrapy.Item):
    title = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    para = Field(input_processor=Join(), output_processor=MapCompose(tags_and_unicode))
    captions = Field(input_processor=Compose(elim_dupes), output_processor=MapCompose(tags_and_unicode))
    images = Field()
    author = Field(input_processor=Join(), output_processor=TakeFirst())
    pubtime = Field(input_processor=MapCompose(iso_time_to_df))
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

class Juxtapoz_Item(scrapy.Item):
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
scrapy crawl juxtapoz
"""
#""https://www.philamuseum.org/collections/results.html?results=18&searchTxt=&searchNameID=&searchClassID=&provenance=0&audio=0&onView=0&searchOrigin=&searchDeptID=1&page=6355&action=post"""

class Artnet_Frontpage_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = Field(input_processor = Join(), output_processor = TakeFirst())
    author = Field(input_processor = Join(), output_processor = TakeFirst())
    blurb = Field(input_processor = Join(), output_processor = TakeFirst())
    link = Field(input_processor = Join(), output_processor = TakeFirst())
    thumbn = Field(input_processor = Join(), output_processor = TakeFirst())
    pubtime = Field(input_processor = Join(), output_processor = TakeFirst())