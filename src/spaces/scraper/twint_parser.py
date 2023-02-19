import collections
from typing import List

import tweepy as tw
from tweepy.cursor import ItemIterator

from src.spaces.data.query import RegionQuery
from src.spaces.data.result import RegionQueryResult, Tweet


class TwintParser:
    def __init__(self):
        # Might not need any changes depending on parsing method
        pass

    def parse_dict(self, tweet_dict: dict):
        tweet_text = tweet_dict['tweet']
        tweet_date = tweet_dict['created_at']
        return Tweet(tweet_date, tweet_text)

