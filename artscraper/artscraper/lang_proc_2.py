import pandas as pd
import pickle
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import os
import nltk
import re
import string

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer


global_path = '~/Desktop/Datasets/art/art_writing'
path = 'artnet_articles'
#path = 'artnet_articles'
#path = 'artnet_articles'
folderpath = os.path.expanduser(os.path.join(global_path, path))

filelist = os.listdir(folderpath)

data = {}
data_df = pd.DataFrame(data)

cleaned_titles = []
cleaned_paras = []

for file in filelist[:5000]:
    filepath = os.path.join(folderpath, file)
    f = open(filepath)  # , encoding='ascii', errors='ignore')
    try:
        j_import = json.load(f)
        j_import = j_import[0]
        # print(j_import)
        # title = j_import['title']
        try:
            para = j_import['para']
            para = para[0]
            para = para.replace("	", "").replace("Follow  on Facebook:", '').replace("\n", ' ')
            para = para.replace("\r", " ")
            para = para.strip()
            # print(para)

            title = j_import['title']
            title = title.replace("	", "").replace("\n", ' ')
            title = title.replace("\r", " ")
            title = title.strip()

            # text = para
            # cleaned_paras.append(text)
            # print(para)

            new_row = {"title": title, "para": para}
            data_df = data_df.append(new_row, ignore_index=True)
            f.close()

        except KeyError:
            f.close()
            pass

    except json.decoder.JSONDecodeError:
        f.close()
        pass

data_df = data_df.set_index('title')

def combine_text(list_of_text):
    '''Takes a list of text and combines them into one large chunk of text.'''
    combined_text = ' '.join(list_of_text)
    return combined_text

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = text.replace('-', ' ')
    text = text.replace("’s ", " ").replace("' ", " ")
    text = text.replace("s’ ", " ").replace("s' ", " ")#remove proper possesives
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
round1 = lambda x: clean_text_round1(x)


def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('new york', 'newyork', text)
    text = re.sub('new year', 'newyear', text)
    text = re.sub('the new museum', 'newmuseum', text)
    #text = text.replace(r'[^\u0020-\u007E]', '')
    return text

round2 = lambda x: clean_text_round2(x)


data_clean = pd.DataFrame(data_df.para.apply(round1))
pd.set_option('display.max_colwidth',500)

data_clean = pd.DataFrame(data_clean.para.apply(round2))

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.para)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index
data_dtm = data_dtm.transpose()
print(data_dtm.head())

#data_dtm.to_pickle(f"{path}doc_term_matrix.pkl")
# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
#data_clean.to_pickle(f"{path}data_clean.pkl")
#pickle.dump(cv, open(f"{path}cv.pkl", "wb"))

# Find the top 30 words in each article
top_dict = {}

for ind, column in enumerate(data_dtm.columns):
    col = data_dtm.iloc[:,[ind]]
    #print(col)
    top = col[column].sort_values(ascending=False)
    top = top.head(30)
    top.set_index = data_dtm.iloc[0, ind]
    top_dict[column]= list(zip(top.index, top.values))
#print(top_dict)

# Print the top 15 words in each article
for title, top_words in top_dict.items():
    print(title)
    print(', '.join([word for word, count in top_words[0:14]]))
    print('---')

# Look at the most common top words --> add them to the stop word list
from collections import Counter

words = []
for article in data_dtm.columns:
    top = [word for (word, count) in top_dict[article]]
    for t in top:
        words.append(t)

#print(words)
#Counter(words).most_common()

# If more than half of the comedians have it as a top word, exclude it from the list
cutoff = data_dtm.shape[1] * (1/3)

add_stop_words = [word for word, count in Counter(words).most_common() if count > cutoff]
print(add_stop_words)

# update document-term matrix with the new list of stop words
# Read in cleaned data
#data_clean = pd.read_pickle('data_clean.pkl')

# Add new stop words
stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)

# Recreate document-term matrix
cv = CountVectorizer(stop_words=stop_words)
data_cv = cv.fit_transform(data_clean.para)
data_stop = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_stop.index = data_clean.index

# Pickle it for later use
pickle.dump(cv, open(f"{path}cv_stop.pkl", "wb"))
data_stop.to_pickle(f"{path}dtm_stop.pkl")

prep = " ".join(data_clean['para'])

wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark3",
               max_font_size=200, random_state=42)

plt.rcParams['figure.figsize'] = [300, 150]

# Create subplots for each comedian
#for index, comedian in enumerate(data.columns):

wc.generate(prep)

#plt.subplot(3, 4, index+1)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
#plt.title(full_names[index])

plt.show()
