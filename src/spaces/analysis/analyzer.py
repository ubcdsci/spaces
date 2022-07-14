import os

import tweepy as tw

from abc import ABC, abstractmethod

from src.spaces.data.activity import RegionActivity
from src.spaces.data.result import RegionQueryResult


class TweetAnalyzer(ABC):
    def __init__(self):

        try:
            consumer_key = os.environ["SPACES_CONSUMER_KEY"]
            consumer_secret = os.environ["SPACES_CONSUMER_SECRET"]
            access_token = os.environ["SPACES_ACCESS_TOKEN"]
            access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
        except KeyError as e:
            print("Your environment variables do not contain the necessary API keys for tweepy.")
            raise e

        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tw.API(auth, wait_on_rate_limit=True)

    """
    Estimate the activity of a queried region at a specified time.
    """

    @abstractmethod
    def analyze(self, result: RegionQueryResult) -> RegionActivity:
        pass
