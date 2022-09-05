import collections
from typing import List

import tweepy as tw
from tweepy.cursor import ItemIterator

from src.spaces.data.query import RegionQuery
from src.spaces.data.result import RegionQueryResult, Tweet


class RegionParser:
    def __init__(self):
        # Might not need any changes depending on parsing method
        pass

    def parse(self, query: RegionQuery, tweets: List[Tweet]):
        return RegionQueryResult(
            query=query,
            tweets=tweets
        )


