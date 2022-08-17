from typing import List

import tweepy as tw

from src.spaces.data.query import RegionQuery
from src.spaces.data.result import RegionQueryResult, Tweet


class RegionParser:
    def __init__(self):
        # Might not need any changes depending on parsing method
        pass

    def parse(self, query: RegionQuery, tweets: tw.Cursor) -> RegionQueryResult:
        out_tweets = []
        for tweet in tweets:
            out_tweets.append(Tweet.from_tweepy(tweet))
        return RegionQueryResult(
            query=query,
            tweets=[tweets]
        )


