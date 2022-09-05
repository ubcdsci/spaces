import random

import pandas as pd
import tweepy as tw
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

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

    # Create the dataset / parse tweets into a histogram
    def train(self, train_result: RegionQueryResult):
        # create list of 366 elements for 0 - 365 days
        year_list = []
        for i in range(365):
            year_list.append([])
        # list created to produce histogram from matplotlib of frequency of each day diff
        all_days = []

        # create list of posted dates
        self._dtst = train_result
        for item in self._dtst.tweets:
            item.post_date = item.post_date.replace(tzinfo=None)
            days_apart = int((item.post_date - self._dtst.query.end_date).days) + 365
            all_days.append(days_apart)
            # add tweet to given index
            year_list[days_apart].append(item)

        # fit list into normal distribution
        mu, std = norm.fit([len(x) for x in year_list])
        return mu, std

        # Convert these counts to a histogram
        days_array = np.array(all_days)
        hist = np.histogram(days_array, bins=365)
        hist_display = plt.hist(days_array, bins = 100)
        plt.show()
        # ...

    def analyze(self, x, mu, std, result: RegionQueryResult):
        probability = norm.pdf(x, mu, std)
        return probability
        # Compare to self.activity_hist
        # return RegionActivity(
        #     query=result.query,
        #     activity=random.random()
        # )
