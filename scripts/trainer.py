"""
This script trains the data obtained
python train.py --start 1 --number 10 > output.json
"""
import json
from multiprocessing import Pool
from collections import defaultdict
import argparse
import sys
import time
from scrapper import get_page_articles, get_article_speech


def create_corpus_item():
    return defaultdict(int)


def create_corpus():
    return defaultdict(create_corpus_item)


def get_texts_per_page(page):
    urls = get_page_articles(page)
    texts = [
            get_article_speech(u).split()
            for u in urls
            ]
    return texts


def join_two_corpus(corpus1, corpus2):
    words = set([*corpus1.keys(), *corpus2.keys()])

    for word in words:
        for value in words:

            if corpus2[word][value] != 0:
                corpus1[word][value] += corpus2[word][value]

    return corpus1


def train(texts, texts_corpus):

    for text in texts:

        for i in range(0, len(text)-1):
            word = text[i]
            next_word = text[i+1]

            texts_corpus[word][next_word] += 1

    return texts_corpus


def positive_int(value):
    value = int(value)

    if value <= 0:
        raise argparse.ArgumentTypeError(f'argument out of range {value} < 0')
    return value


if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('--start',
                        type=positive_int,
                        help="index of page starting the training",
                        default=1
                        )
    parser.add_argument('--number',
                        type=positive_int,
                        help="amount of pages to be trained with",
                        default=10
                        )

    args = parser.parse_args()

    articles = []
    with Pool(4) as pool:
        for articles_per_page in pool.imap(
                                        get_texts_per_page,
                                        range(
                                            args.start,
                                            args.start + args.number
                                            )
                                        ):
            articles.extend(articles_per_page)

    corpus = create_corpus()
    train(articles,  corpus)

    print(json.dumps(corpus))
    print(f'--- {time.time() - start_time} secconds ---', file=sys.stderr)
