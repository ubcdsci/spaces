from abc import ABC

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn import mixture


from src.spaces.analysis.analyzer import TweetAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.result import RegionQueryResult

from src.spaces.analysis.analyzer import TweetAnalyzer
from src.spaces.data.result import RegionQueryResult


class MixtureAnalyzer(TweetAnalyzer):
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

        data= [len(x) for x in year_list]
        data_array = np.array(data).reshape(-1,1)
        mixture_gaussian = mixture.GaussianMixture(n_components=2, covariance_type='full').fit(data_array)
        x= np.array(np.linspace(0, 8000, 50)).reshape(-1,1)
        y= mixture_gaussian.score_samples(x)
        means = mixture_gaussian.means_
        sigma = np.sqrt(mixture_gaussian.covariances_)

        data_hist = plt.hist(data_array, density= True, bins = 7)
        return x,y, means, sigma, data_hist


    def analyze(self,x, result: RegionQueryResult, mu, sd):
        inactive_mu = mu[0][0]
        active_mu = mu[1][0]
        inactive_sd = sd[0][0][0]
        active_sd = sd[1][0][0]
        probability_inactive = norm.pdf(x, inactive_mu, inactive_sd)
        probability_active = norm.pdf(x, active_mu, active_sd)
        return probability_inactive, probability_active
        # Compare to self.activity_hist
        # return RegionActivity(
        #     query=result.query,
        #     activity=random.random()
        # )



