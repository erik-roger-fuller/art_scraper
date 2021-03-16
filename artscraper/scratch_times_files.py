import csv
from csv import DictReader

import os

filename1 = f"Nytimes_arts_freq_of_arts_2000_2021.csv"
filename2 = f"Nytimes_arts_final_arts_links_2000_2021.csv"

filepath1 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art', filename1)

filepath2 = os.path.join(os.path.expanduser('~'), 'Desktop/Datasets/art', filename2)
urls = []
with open(filepath2, newline='') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    for row in read_csv:
        link_dump = row[1]
        link_dump = link_dump.replace("[","").replace("]","").replace("'","")
        #print(link_dump)
        #link_dump = (', '.join(row))
        links = link_dump.split(", ")
        #print(links)
        for link in links:
            link = link.replace(" ", "")
            if link == "":
                pass
            else:
                # print(link)
                urls.append(link)
#urls.reverse()
print(urls[333:400])
#print(len(urls))

