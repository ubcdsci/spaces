from abc import ABC

import string

from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer

from src.spaces.analysis.analyzer import TweetAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.result import RegionQueryResult


class SentenceAnalyzer(TweetAnalyzer, ABC):
    def __init__(self):
        pass

    # preprocess & import data
    def train(self, train_result: RegionQueryResult):
        data = []
        stop_words = set(stopwords.words('english'))
        tweets_text = ''
        for text in train_result.tweets:
            tweets_text = tweets_text + text.tweet_text
        # replaces escape character with space
        tweets_edit = tweets_text.replace("\n", " ")
        for tweet in sent_tokenize(tweets_edit):
            # remove punctuations from line
            tweet.translate(str.maketrans('', '', string.punctuation))
            # remove stop words
            if tweet not in stop_words:
                for token in word_tokenize(tweet):
                    data.append(token.lower())
        return data

    def analyze(self, sentences: [str]) -> RegionActivity:
        pass
