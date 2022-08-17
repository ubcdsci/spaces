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

scraper = RegionScraper()
parser = RegionParser()

dataset_start = datetime.datetime.now() - datetime.timedelta(days=365)

# Placeholders, get the tweets from last week to today
start_date = datetime.datetime.now() - datetime.timedelta(days=7)
end_date = datetime.datetime.now()

analyzer = ExampleAnalyzer()

results: List[RegionActivity] = []

# for region in regions:
#     dtst_query = RegionQuery(
#         region=region,
#         start_date=dataset_start,
#         end_date=end_date
#     )
# dtst_tweets: tw.Cursor = scraper.compile_tweets(dtst_query)
# parsed_dtst_tweets: RegionQueryResult = parser.parse(dtst_query, dtst_tweets)
# print(dtst_tweets)
#
#
# analyze_query = RegionQuery(
#     region=region,
#     start_date=start_date,
#     end_date=end_date
# )
# analyze_tweets: tw.Cursor = scraper.compile_tweets(analyze_query)
# parsed_tweets: RegionQueryResult = parser.parse(analyze_query, analyze_tweets)
#
# results.append(analyzer.analyze(parsed_tweets))
#
# print(results)
# print(analyzer.train(parsed_dtst_tweets))

name_list = ['Aulavik', 'Auyuittuq', 'Banff', 'Bruce Peninsula', 'Cape Breton Highlands', 'Elk Island', 'Forillon',
             'Fundy', 'Georgian Bay Islands', 'Glacier', 'Grasslands', 'Gros Morne', 'Gulf Islands',
             'Gwaii Haanas', 'Ivvavik', 'Jasper', 'Kejimkujik', 'Kluane', 'Kootenay', 'Kouchibouguac', 'La Mauricie',
             'Lake Huron', 'Lake Louise', 'Lake Superior', 'Mingan Archipelago', 'Mont-Tremblant',
             'Mount Logan', 'Mount Revelstoke', 'Moraine Lake', "Naats'ihch'oh", 'Nahanni', 'Niagara Falls',
             'Pacific Rim', 'Point Pelee', 'Prince Albert', 'Prince Edward Island', 'Pukaskwa', 'Quttinirpaaq',
             'Riding Mountain', 'Sable Island', 'Sirmilik', 'Terra Nova', 'Thousand Islands', 'Torngat Mountains',
             'Tuktut Nogait', 'Ukkusiksalik', 'Vuntut', 'Wapusk', 'Waterton Lakes', 'Whistler Blackcomb',
             'Wood Buffalo', 'Yoho']

region_fake = []
for name in name_list:
    region_fake.append(Region(
        name=name,
        region_type=RegionType.OUTDOOR,
        latitude=100,
        longitude=-35,
        radius=0.5
    ))

# keep to datetime -> note
merged_result = RegionQueryResult(
    query=RegionQuery(region=region_fake[0], start_date=dataset_start, end_date=end_date),
    tweets=[])

# for index, region in enumerate(region_fake):
#     date_offset = datetime.timedelta(weeks=index)
#     query_fake = RegionQuery(
#         region=region,
#         start_date=start_date,
#         end_date=end_date
#     )
#     fake_tweets = scraper.compile_tweets(query_fake)
#     for tweet in fake_tweets:
#         tweet.created_at -= date_offset
#     fake_parsed_tweets: RegionQueryResult = parser.parse(query_fake, fake_tweets)
#     merged_result.tweets += fake_parsed_tweets.tweets

# test -> checking if retrieving tweet dates and adjusting properly
# test_fake = scraper.compile_tweets(RegionQuery(region='stanley park', start_date=start_date,
#                                                end_date=end_date))
# for tweet in test_fake:
#     tweet.created_at -= datetime.timedelta(weeks=1)
#     print(tweet.created_at)
# fake_parsed_tweets = parser.parse(RegionQuery(region='stanley park', start_date=start_date, end_date=end_date),
#                                   test_fake)
# merged_result.tweets += fake_parsed_tweets.tweets

# saving into pickle file
# file_to_store = open("stored_result.pickle", "wb")
# pickle.dump(merged_result, file_to_store)
# file_to_store.close()

# reading from pickle file
file_to_read = open("stored_result.pickle", "rb")
loaded_result = pickle.load(file_to_read)
file_to_read.close()
print(loaded_result)
