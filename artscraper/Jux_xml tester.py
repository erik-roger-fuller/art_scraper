import datetime
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
import time
from csv import DictWriter
import os

filename1 = 'juxtapoz_sitemap.xml'
filepath1 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art/art_writing/juxtapoz', filename1)

urls = []
with open(filepath1, 'r') as read_path:
    soup = BeautifulSoup(read_path, 'lxml' )
    linx = soup.select('loc')
    for link in linx:
        link = link.get_text()
        print(link)
        urls.append(link)
urls = urls[:-22]
print(urls)
