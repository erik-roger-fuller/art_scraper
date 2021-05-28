from scrapy.exporters import JsonLinesItemExporter, JsonItemExporter

from itemadapter import ItemAdapter
from datetime import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import os
import re


class Article_Pipeline:
    def open_spider(self, spider):
        self.title_to_exporter = {}
        self.files = []

    def close_exporters(self):
        for title, exporter in self.title_to_exporter.items():
            exporter.finish_exporting()
            self.title_to_exporter = {}


    def close_files(self):
        for i, f in enumerate(self.files):
            f.close()
            self.files = []

    def close_spider(self, spider):
        self.close_exporters()
        self.close_files()
        #for exporter in self.title_to_exporter.values():
        #exporter.finish_exporting()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)

        title = adapter.get('title')
        title = str(title)

        pubtime = adapter.get('pubtime')
        #pubtime = str(pubtime)
        pubtime_m = datetime.strftime(pubtime, "%Y_%m_%d")

        source = adapter.get('source')
        source = str(source)

        url = adapter.get("url")
        url = str(url)

        if title not in self.title_to_exporter:
            if source == "artagenda":

                url = url.split("/")
                #urlname = url[-1]_{url[-2]}
                filename = f"{pubtime_m}_{url[-1]}_{source}"
            else:
                if len(title)<55:
                    filename = f"{pubtime_m}_{title}_{source}"
                else:
                    filename = f"{pubtime_m}_{title[:55]}_{source}"

            filename = filename_clean(filename)
            filename = f"{filename}.json"
            #linux
            #filepath = os.path.join(os.path.expanduser('~'),'Desktop/scrapy/articles_dump', filename)

            #win
            filepath = os.path.join(os.path.expanduser('~'), 'PycharmProjects/art_scraper/artscraper/articles_dump', filename )

            print("Saved:   " + filename_final)
            self.close_exporters() #shutsdowns old
            self.close_files() #ditto
            f = open(filepath, 'wb' ) #open statement
            self.files.append(f) #adds file to files bin
            exporter = JsonItemExporter(f)
            exporter.export_empty_fields=True
            exporter.start_exporting()
            self.title_to_exporter[title] = exporter
        return self.title_to_exporter[title]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item


def filename_clean(filename):
    filename = filename.strip()
    filename = re.sub('[^0-9a-zA-Z ]+', ' ', filename)
    filename = re.sub('[ _]+', '_', filename)
    #filename = re.sub('_+', '_', filename)
    return filename

class Artnet_Headline_Pipeline:
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        #print("Pipeline test:  " + item['blurb'][0])
        return item

    def __init__(self):
        self.file = open("metadata.jsonl", 'wb')
        self.exporter = JsonLinesItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

"""
    newname = filename.replace("-", "_")
    newname = newname.replace(":", "_")
    newname = newname.replace(";", "")

    #spaces
    newname = newname.replace("  ", "_")
    newname = newname.replace(" ", "_")

    #funny business
    newname = newname.replace('#', '')
    newname = newname.replace('%', '')
    newname = newname.replace('*', '')
    newname = newname.replace('<', '')
    newname = newname.replace('>', '')
    newname = newname.replace('*', '')
    newname = newname.replace('?', '')
    newname = newname.replace("+", "_")

    #things that look like bananas
    newname = newname.replace("(", "")
    newname = newname.replace(")", "")
    newname = newname.replace("[", "")
    newname = newname.replace("]", "")
    newname = newname.replace("{", "")
    newname = newname.replace("}", "")
    newname = newname.replace("/", "").replace("\\", "").replace("|", "")

    #things that look like whiskers
    newname = newname.replace("'", "")
    newname = newname.replace('"', "")
    newname = newname.replace("’", "")
    newname = newname.replace(".", "_")
    newname = newname.replace(",", "_")

    newname = newname.replace("`", "").replace("'", "").replace('"', "")
    newname = newname.replace("__", "_")
    #newname = re.sub(r'[T][\d][\d][_][\d][\d][_][\d][\d][_][\d][\d][_][\d][\d][_]', '_', newname)
    return newname



#other components of reconfiguarble pipelines


    def process_item(self, item, spider):
        #self.exporter.export_item(item)
        print("Pipeline test:  " + item['para'])
        name = item['para']
        return item

    def __init__(self):
        self.file = open("test_article_json", 'wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

"""
