from scrapy.exporters import JsonLinesItemExporter, JsonItemExporter

from itemadapter import ItemAdapter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

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
        pubtime = str(pubtime)

        source = adapter.get('source')
        source = str(source)

        if title not in self.title_to_exporter:
            filename = str(pubtime + "_" + title + '_' + source )
            filename = filename_clean(filename)
            filename_final = str(filename + '.json')
            filepath = os.path.join(os.path.expanduser('~'),
                                    'Desktop/scrapy/articles_dump', filename)

            print("Saved:   " + filename)
            self.close_exporters() #shutsdowns old
            self.close_files() #ditto
            f = open(filepath, 'wb' ) #open statement
            self.files.append(f) #adds file to files bin
            exporter = JsonItemExporter(f)
            exporter.start_exporting()
            self.title_to_exporter[title] = exporter
        return self.title_to_exporter[title]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item


def filename_clean(filename):
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

    #things that look like bananas
    newname = newname.replace("(", "")
    newname = newname.replace(")", "")
    newname = newname.replace("[", "")
    newname = newname.replace("]", "")
    newname = newname.replace("{", "")
    newname = newname.replace("}", "")

    #things that look like whiskers
    newname = newname.replace("'", "")
    newname = newname.replace('"', "")

    newname = newname.replace(".", "_")
    newname = newname.replace(",", "_")
    newfilename = newname.replace("+", "_")
    return newfilename


"""
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



class Artnet_Headline_Pipeline:
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        #print("Pipeline test:  " + item['blurb'][0])
        return item

    def __init__(self):
        self.file = open("artnetfrontpagetoday.jsonl", 'wb')
        self.exporter = JsonLinesItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
"""
