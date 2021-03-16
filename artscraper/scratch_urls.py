import datetime
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
import time
from csv import DictWriter
import os


branch = "arts"

sitemap_urls = []
freq_of_arts, final_urls = [] , []

base_url = "https://www.nytimes.com/"

dates = []

enddate = datetime.date.today()
startdate = datetime.date(2000, 1, 1)
diff = enddate - startdate
for i in range(diff.days +1):
    day = startdate + timedelta(days=i)
    #print(day)
    cdate = datetime.datetime.strftime(day, "%Y/%m/%d/")
    dates.append(cdate)

dates.reverse()

for url_date in dates:
    sitemap_url = str(base_url + "sitemap/" + url_date)
    sitemap_urls.append(sitemap_url)
#print(sitemap_urls)


def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)
        print(f"Saved line : \n {dict_of_elem} \n at {file_name}")

filename1 = f"Nytimes_arts_freq_of_arts_2000_2021.csv"
filename2 = f"Nytimes_arts_final_arts_links_2000_2021.csv"

filepath1 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art', filename1)

filepath2 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art', filename2)

"""retrieval loop"""
for i, sitemap_url in enumerate(sitemap_urls):
    #init
    freq_of_arts, final_urls = [], []

    time.sleep(.015)

    r = requests.get(sitemap_url)
    print(f"PAGE: {i}\t  REQUESTED: \t{r.url} \t GOT: {r.status_code} " )
    soup = BeautifulSoup(r.content, "html.parser")

    day2 = sitemap_url[-11:-1]
    arts = 0
    not_arts = 0

    li = soup.select("li > a[href]")
    for link in li:
        link = link.get('href')

        if link [34:40] == "/arts/":
            print(link)
            final_urls.append(link)
            arts += 1
        else:
            not_arts += 1


    append_dict_as_row(file_name=filepath1, dict_of_elem={"day": day2 , "yes_arts" : arts , "no_arts" : not_arts} ,
                       field_names=["day","yes_arts","no_arts",])


    append_dict_as_row(file_name=filepath2, dict_of_elem={"day": day2 , "links" : final_urls } ,
                       field_names=["day","links"])


print("finished!")





"""
        elif link[34:41] == "/books/":
            print(link)
        elif link [34:42] == "/movies/":
            print(link)
        elif link [34:42] == "/theatre/":
            print(link)
        else:
            print("not     "+ link)
"""