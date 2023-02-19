import datetime
import random
import string
from typing import List

import os

import numpy as np
import tweepy as tw
from matplotlib import pyplot as plt
from scipy.stats import norm

from src.spaces.analysis.gaussian_analyzer import ExampleAnalyzer
from src.spaces.analysis.mixture_analyzer import MixtureAnalyzer
from src.spaces.analysis.sentence_analyzer import SentenceAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.query import RegionQuery
from src.spaces.data.region import Region
from src.spaces.data.region_type import RegionType
from src.spaces.data.result import RegionQueryResult
from src.spaces.scraper.parser import RegionParser
from src.spaces.scraper.scraper import RegionScraper
import pickle

analyzer = ExampleAnalyzer()
mixed_analyzer = MixtureAnalyzer()
sentence_analyzer = SentenceAnalyzer()

# reading from pickle file
for index in range(0, 8):
    if index == 0:
        first_file = open("../stored_results_0.pickle", "rb")
        final_results = pickle.load(first_file)
        first_file.close()
    else:
        file_to_read = open("../stored_results_" + str(index) + ".pickle", "rb")
        loaded_result = pickle.load(file_to_read)
        final_results.tweets += loaded_result.tweets
        file_to_read.close()
# print(final_results)

# whistler analyzing
whistler_file = open("../whistler.pickle", "rb")
whistler_results = pickle.load(whistler_file)
whistler_file.close()

# sentence analyzing
sentences = sentence_analyzer.train(whistler_results)
print(sentence_analyzer.analyze(sentences))

# mixture analyzing
x, y, mu, sigma, array = mixed_analyzer.train(final_results)
activity = mixed_analyzer.analyze(50, final_results, mu, sigma)
# print(activity)

# data distribution of number of tweets
# data_hist = plt.hist(array, bins=15, alpha=0.7, rwidth=0.8, color='#008B8B')
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Number of Tweets Per Day')
# plt.ylabel('Frequency')
# plt.title('Data Distribution of Daily Number of Tweets')
# plt.show()
#
# # gaussian plot of log likelihood -> measure of goodness of fit for models
# gaussian_plot = plt.plot(x, y, color='m')
# plt.ylabel("Log Likelihood")
# plt.xlabel("Number of Tweets Per Day")
# plt.title("Mixture Gaussian Likelihood Given Number of Tweets")
# plt.show()
#
# # gaussian scatter plot
# plt.scatter(x,y)
# plt.show()

#whistler file reading
# file_to_read = open('/Users/eo03/Develop/spaces/src/spaces/whistler.pickle', "rb")
# whistler_result = pickle.load(file_to_read)
# print(whistler_result.tweets)

