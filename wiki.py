import bs4 as bs
import requests
import re
from collections import Counter
from heapq import nlargest

import spacy
nlp = spacy.load('en_core_web_sm')

def search(search_query, no_of_sentences):
    headers = {'User-Agent': 'github.com/nishan7'}
    url = 'https://en.wikipedia.org/w/rest.php/v1/search/page'
    search_result = requests.get(url, headers=headers, params={'q': search_query, 'limit': 1}).json()['pages'][0]

    page = requests.get('https://en.wikipedia.org/w/rest.php/v1/page/{}/with_html'.format(search_result['key']),
                        headers=headers).json()

    soup = bs.BeautifulSoup(page['html'], 'lxml')

    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text

    # Data Cleaning
    text = re.sub(r'\[.*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Create Doc object
    text_nlp = nlp(text)

    # Get the  Word Count
    words = [token.text.lower() for token in text_nlp if token.is_alpha and not token.is_stop]
    word_count = Counter(words)

    # Get the weighted Word Count
    max_count = max(word_count.values())
    for word in word_count.keys():
        word_count[word] /= max_count

    # Get the sentences Score, with index of the sentences from the start , so order of sentence in summary is same as the document
    sentences_score = {}
    for index, sentence in enumerate(text_nlp.sents):
        for word in sentence:
            word = word.text.lower()
            #         print(word, word in word_count.keys())
            if word in word_count.keys():
                if word in sentences_score.keys():
                    sentences_score[sentence][0] += word_count[word]
                else:
                    sentences_score[sentence] = [word_count[word], index]

    topn = nlargest(no_of_sentences, sentences_score.items(),
                    lambda x: x[1][0])  # 1 index is for values and 0 for word_count
    topn.sort(key=lambda x: x[1][1])  # 1 index is for values and 1 is for index of sentence in the doc,

    print(page['title'] + '\n')
    print('-' * 10 + ' Summary ' + '-' * 10)
    for n in topn:
        print(n[0])


search(search_query='Earth', no_of_sentences=5)
