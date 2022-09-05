import datetime
import random
import string
from typing import List

import os
import tweepy as tw

from src.spaces.analysis.example_analyzer import ExampleAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.query import RegionQuery
from src.spaces.data.region import Region
from src.spaces.data.region_type import RegionType
from src.spaces.data.result import RegionQueryResult
from src.spaces.scraper.parser import RegionParser
from src.spaces.scraper.scraper import RegionScraper
import pickle

analyzer = ExampleAnalyzer()

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
norm_mu, norm_std = analyzer.train(final_results)
print(norm_mu, norm_std)
x = 600
analyzed_prob = analyzer.analyze(x, norm_mu, norm_std, final_results)
print(analyzed_prob)

