import datetime
import json
import random
import string
from typing import List

import os
import tweepy as tw

from src.spaces.analysis.gaussian_analyzer import ExampleAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.query import RegionQuery
from src.spaces.data.region import Region
from src.spaces.data.region_type import RegionType
from src.spaces.data.result import RegionQueryResult
from src.spaces.data.tweet import Tweet
from src.spaces.scraper.parser import RegionParser
from src.spaces.scraper.scraper import RegionScraper
import pickle
import twint as tn
import nest_asyncio

from src.spaces.scraper.twint_parser import TwintParser
from src.spaces.scraper.twint_scraper import TwintScraper

nest_asyncio.apply()
scraper = RegionScraper()
parser = RegionParser()
twint_parser = TwintParser()

dataset_start = datetime.datetime.now() - datetime.timedelta(days=365)

# Placeholders, get the tweets from last week to today
start_date = datetime.datetime.now() - datetime.timedelta(days=7)
end_date = datetime.datetime.now()

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

stored_result_list_0 = ['Aulavik', 'Auyuittuq', 'Balaclava Park', 'Bruce Peninsula', 'Cape Breton Highlands',
                        'Elk Island',
                        'Forillon', 'Fundy', 'Georgian Bay Islands', 'Galiano Island', 'Gibsons', 'Gros Morne',
                        'Gulf Islands',
                        'Gwaii Haanas', 'Ivvavik', 'Jelounaifa', 'Kelowna', 'Kluane']
stored_result_list_1 = ['Kootenay']
stored_result_list_2 = ['Kamloops']
stored_result_list_3 = ['La Mauricie', 'Lake Huron', 'Lake Louise', 'Lake Superior', 'Mingan Archipelago',
                        'Mont-Tremblant',
                        'Mount Logan', 'Mount Revelstoke']
stored_result_list_4 = ['Moraine Lake', "Nairn Falls", 'Nahanni', 'Niagara Falls']
stored_result_list_5 = ['Pacific Rim', 'Point Pelee', 'Prince Albert', 'Prince Edward Island', 'Porteau Cove',
                        'Qualicum Beach',
                        'Riding Mountain', 'Sable Island', 'Sirmilik']
stored_result_list_6 = ['Terra Nova', 'Thousand Islands', 'Torngat Mountains',
                        'Tofino', 'Union Bay', 'Vuntut']
name_list = ['White Lake', 'Waterton Lakes', 'Whistler Blackcomb', 'Wood Buffalo', 'Yoho']

# region_fake = []
# for name in name_list:
#     region_fake.append(Region(
#         name=name,
#         region_type=RegionType.OUTDOOR,
#         latitude=100,
#         longitude=-35,
#         radius=0.5
#     ))
#
# # keep to datetime -> note
# merged_result = RegionQueryResult(
#     query=RegionQuery(region=region_fake[0], start_date=dataset_start, end_date=end_date),
#     tweets=[])
#
# for index, region in enumerate(region_fake):
#     out_list = []
#     print(region)
#     date_offset = datetime.timedelta(weeks=index+47)
#     query_fake = RegionQuery(
#         region=region,
#         start_date=start_date,
#         end_date=end_date
#     )
#     fake_tweets = scraper.compile_tweets(query_fake)
#     for tweet in fake_tweets:
#         tweet.created_at -= date_offset
#         out_list.append(Tweet.from_tweepy(tweet))
#     fake_parsed_tweets: RegionQueryResult= parser.parse(query_fake, out_list)
#     # print(fake_parsed_tweets)
#     merged_result.tweets += fake_parsed_tweets.tweets
#
# #
# # saving into pickle file
# file_to_store = open("../stored_results_7.pickle", "wb")
# pickle.dump(merged_result, file_to_store)
# file_to_store.close()
# print("Saved")

# for i in range(1, 366):
#     twint_query = RegionQuery(region="Whistler", start_date=datetime.datetime.now() - datetime.timedelta(days=i),
#                               end_date=datetime.datetime.now() - datetime.timedelta(days=i-1))
#     twint_scraper = TwintScraper()
#     test_scrape = twint_scraper.compile_tweets(twint_query, '../whistler_twint.json')

# creating whistler region query result
whistler_start = datetime.datetime.strptime('2021-11-09', '%Y-%m-%d')
whistler_end = datetime.datetime.strptime('2022-11-09', '%Y-%m-%d')
whistler_result = RegionQueryResult(RegionQuery(region='Whistler',start_date=whistler_start, end_date=whistler_end),
                                    tweets=[])
json_file_path = '/Users/eo03/Develop/spaces/src/spaces/whistler_twint.json'

# parsing twint json into data structure Tweet & saving to pickle file, removing p
whistler_tweets = []
with open(json_file_path) as f:
    for line in f:
       entry = json.loads(line)
       tweet = twint_parser.parse_dict(entry)
       whistler_tweets.append(tweet)
whistler_result.tweets += whistler_tweets
whistler_file_store = open('/Users/eo03/Develop/spaces/src/spaces/whistler.pickle', 'wb')
pickle.dump(whistler_result, whistler_file_store)
whistler_file_store.close()
print("saved whistler")
os.remove('/Users/eo03/Develop/spaces/src/spaces/whistler_twint.json')






