sitemap_urls = []
for urlno in range(1,71):
    urlbase = 'https://www.artforum.com/sitemap/articles?page='
    urlfinal = urlbase + str(urlno)
    sitemap_urls.append(urlfinal)
sitemap_urls.reverse()
print(sitemap_urls)

def fetch_urls(self):
    sitemap_urls = []
    for urlno in range(1, 71):
        urlbase = 'https://www.artforum.com/sitemap/articles?page='
        urlfinal = urlbase + str(urlno)
        sitemap_urls.append(urlfinal)
    return sitemap_urls
"""
sitemap_urls = ['https://www.artforum.com/sitemap/articles?page=1',
                'https://www.artforum.com/sitemap/articles?page=2',
                'https://www.artforum.com/sitemap/articles?page=3',
                'https://www.artforum.com/sitemap/articles?page=4',
                'https://www.artforum.com/sitemap/articles?page=5',
                'https://www.artforum.com/sitemap/articles?page=6',
                'https://www.artforum.com/sitemap/articles?page=7',
                'https://www.artforum.com/sitemap/articles?page=8',
                'https://www.artforum.com/sitemap/articles?page=9',
                'https://www.artforum.com/sitemap/articles?page=10',
                'https://www.artforum.com/sitemap/articles?page=11',
                'https://www.artforum.com/sitemap/articles?page=12',
                'https://www.artforum.com/sitemap/articles?page=13',
                'https://www.artforum.com/sitemap/articles?page=14',
                'https://www.artforum.com/sitemap/articles?page=15',
                'https://www.artforum.com/sitemap/articles?page=16',
                'https://www.artforum.com/sitemap/articles?page=17',
                'https://www.artforum.com/sitemap/articles?page=18',
                'https://www.artforum.com/sitemap/articles?page=19',
                'https://www.artforum.com/sitemap/articles?page=20',
                'https://www.artforum.com/sitemap/articles?page=21',
                'https://www.artforum.com/sitemap/articles?page=22',
                'https://www.artforum.com/sitemap/articles?page=23',
                'https://www.artforum.com/sitemap/articles?page=24',
                'https://www.artforum.com/sitemap/articles?page=25',
                'https://www.artforum.com/sitemap/articles?page=26',
                'https://www.artforum.com/sitemap/articles?page=27',
                'https://www.artforum.com/sitemap/articles?page=28',
                'https://www.artforum.com/sitemap/articles?page=29',
                'https://www.artforum.com/sitemap/articles?page=30',
                'https://www.artforum.com/sitemap/articles?page=31',
                'https://www.artforum.com/sitemap/articles?page=32',
                'https://www.artforum.com/sitemap/articles?page=33',
                'https://www.artforum.com/sitemap/articles?page=34',
                'https://www.artforum.com/sitemap/articles?page=35',
                'https://www.artforum.com/sitemap/articles?page=36',
                'https://www.artforum.com/sitemap/articles?page=37',
                'https://www.artforum.com/sitemap/articles?page=38',
                'https://www.artforum.com/sitemap/articles?page=39',
                'https://www.artforum.com/sitemap/articles?page=40',
                'https://www.artforum.com/sitemap/articles?page=41',
                'https://www.artforum.com/sitemap/articles?page=42',
                'https://www.artforum.com/sitemap/articles?page=43',
                'https://www.artforum.com/sitemap/articles?page=44',
                'https://www.artforum.com/sitemap/articles?page=45',
                'https://www.artforum.com/sitemap/articles?page=46',
                'https://www.artforum.com/sitemap/articles?page=47',
                'https://www.artforum.com/sitemap/articles?page=48',
                'https://www.artforum.com/sitemap/articles?page=49',
                'https://www.artforum.com/sitemap/articles?page=50',
                'https://www.artforum.com/sitemap/articles?page=51',
                'https://www.artforum.com/sitemap/articles?page=52',
                'https://www.artforum.com/sitemap/articles?page=53',
                'https://www.artforum.com/sitemap/articles?page=54',
                'https://www.artforum.com/sitemap/articles?page=55',
                'https://www.artforum.com/sitemap/articles?page=56',
                'https://www.artforum.com/sitemap/articles?page=57',
                'https://www.artforum.com/sitemap/articles?page=58',
                'https://www.artforum.com/sitemap/articles?page=59',
                'https://www.artforum.com/sitemap/articles?page=60',
                'https://www.artforum.com/sitemap/articles?page=61',
                'https://www.artforum.com/sitemap/articles?page=62',
                'https://www.artforum.com/sitemap/articles?page=63',
                'https://www.artforum.com/sitemap/articles?page=64',
                'https://www.artforum.com/sitemap/articles?page=65',
                'https://www.artforum.com/sitemap/articles?page=66',
                'https://www.artforum.com/sitemap/articles?page=67',
                'https://www.artforum.com/sitemap/articles?page=68',
                'https://www.artforum.com/sitemap/articles?page=69',
                'https://www.artforum.com/sitemap/articles?page=70']
"""