import random

import pandas as pd
import tweepy as tw

from src.spaces.analysis.analyzer import TweetAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.result import RegionQueryResult

"""
Example analyzer to estimate the activity in a specific region. Produces a random number for the requested region
"""


class ExampleAnalyzer(TweetAnalyzer):
    def __init__(self):
        # Histogram of activity
        self._activity_hist = ...
        self._dtst = None

    def train(self, train_result: RegionQueryResult):
        # Create the dataset / parse tweets into a histogram
        self._dtst = train_result
        tweet_list = []

        for tweet in self._dtst.tweets:
            tweet_list.append(tweet)


        # # Count up tweets for each day

        # Convert these counts to a histogram
        # ...

    def analyze(self, result: RegionQueryResult) -> RegionActivity:
        # Compare to self.activity_hist
        return RegionActivity(
            query=result.query,
            activity=random.random()
        )
