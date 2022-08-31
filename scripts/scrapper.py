"""
This Module script returns text from article, also returns article list from a page
"""
import requests
from bs4 import BeautifulSoup
import unicodedata
import sys

BASE_URL = "https://lopezobrador.org.mx/transcripciones"

def get_page_articles(page=1):
    """
    This function gets page links from certain page
    page 1 is the latest transcript, the greater the page the oldest entry
    """

    links = []
    url = f"{BASE_URL}/page/{page}/"

    print(f'requesting {url} page.', file=sys.stderr)
    # we perform a GET REQUEST
    response = requests.get(url)

    # If response has OK status continue, else return the empty link list
    if response:
        # we get the text response from the request
        response_text = response.text

        # we use lxml decoder
        soup = BeautifulSoup(response_text, 'lxml')

        #  div.entry-post > h2 > a
        links_elements = soup.select('div.entry-post > h2 > a')

        links = [x['href'] for x in links_elements]

    return links


def get_article_speech(article_url):
    """
    This functions gets amlo speeches
    """

    speech = ''
    print(f'requesting {article_url} page.', file=sys.stderr)
    # we perform a GET REQUEST
    response = requests.get(article_url)

    # If response has OK status continue, else return the empty speech
    if response:
        # we get the text response from the request
        response_text = response.text

        # we use lxml decoder
        soup = BeautifulSoup(response_text, 'lxml')

        # p.p1
        speech_elements = soup.select('div.entry-content p')

        paragraphs = []

        amlo = False
        pamlo = 'PRESIDENTE ANDRÉS MANUEL LÓPEZ OBRADOR:'
        for speech_elem in speech_elements:
            if (len(speech_elem.contents) > 1 and
                    pamlo in speech_elem.contents[0].getText()):
                amlo = True
            elif (len(speech_elem.contents) > 1 and
                    pamlo not in speech_elem.contents[0].getText()):
                amlo = False

            if amlo:
                texts_elements = [
                        s for s in speech_elem.contents
                        if pamlo not in s.getText()
                        ]
                texts = ' '.join([s.getText() for s in texts_elements])

                if '+++++' not in texts:
                    paragraphs.append(texts)

        speech = ' '.join(paragraphs)

    speech = unicodedata.normalize('NFC', speech)

    return speech


if __name__ == '__main__':
    article_urls = get_page_articles()

    print(get_article_speech(article_urls[0]), file=sys.stderr)
    # articles = [get_page_articles(url) for url in article_urls]
