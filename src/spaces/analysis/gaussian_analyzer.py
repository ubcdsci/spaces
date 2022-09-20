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
        self._mu = 0
        self._std = 1

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
        self._mu, self._std = norm.fit([len(x) for x in year_list])

        # Convert these counts to a histogram
        days_array = np.array(all_days)
        return days_array
        # t= np.linspace(-1500, 2000, 150)
        # return plt.plot(t, norm.pdf(t, mu, std))
        # plt.show()
        # hist = np.histogram(days_array, bins=365)
        # plt.hist(year_list, bins=50, density=True, alpha=0.5)
        # ...

    def analyze(self, result: RegionQueryResult):
        probability = norm.cdf(len(result.tweets), self._mu, self._std)
        return probability > 0.9
        # Compare to self.activity_hist
        # return RegionActivity(
        #     query=result.query,
        #     activity=random.random()
        # )
