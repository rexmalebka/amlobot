import json
import argparse
from collections import defaultdict
import random

def json_type(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
        return data

def generate(word, corpus, random_ratio):
    if random.random() > random_ratio:
        best = max(corpus[word], key=corpus[word].get)
    else:
        best = random.choice(list(args.corpus[word].keys()))
    return  best

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('start_word', type=str, help="word start")
    parser.add_argument('num_words', type=int, help="word start")
    parser.add_argument('corpus', type=json_type,help="json generated with the training")
    parser.add_argument('--random_ratio', type=float, help="probability to choose a random word", default=0)

    args = parser.parse_args()
    args.corpus

    if args.start_word not in args.corpus:
        args.start_word = random.choice(list(args.corpus.keys()))


    word = args.start_word
    text = word

    for i in range(args.num_words):
        word = generate(word, args.corpus, args.random_ratio)
        text += f' {word}'

    print(text)
        

