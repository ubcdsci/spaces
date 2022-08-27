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

stored_result_list = ['Aulavik', 'Auyuittuq', 'Balaclava Park', 'Bruce Peninsula', 'Cape Breton Highlands', 'Elk Island',
             'Forillon', 'Fundy', 'Georgian Bay Islands', 'Galiano Island', 'Gibsons', 'Gros Morne', 'Gulf Islands',
             'Gwaii Haanas', 'Ivvavik', 'Jelounaifa', 'Kelowna', 'Kluane']
stored_result_list_1 = ['Kootenay']
stored_result_list_2 = ['Kamloops']
stored_result_list_3 = ['La Mauricie','Lake Huron', 'Lake Louise', 'Lake Superior', 'Mingan Archipelago', 'Mont-Tremblant',
             'Mount Logan', 'Mount Revelstoke']
stored_result_list_4  = ['Moraine Lake', "Nairn Falls", 'Nahanni', 'Niagara Falls']
stored_result_list_5 = ['Pacific Rim', 'Point Pelee', 'Prince Albert', 'Prince Edward Island', 'Porteau Cove', 'Qualicum Beach',
             'Riding Mountain', 'Sable Island', 'Sirmilik']
stored_result_list_6 = ['Terra Nova', 'Thousand Islands', 'Torngat Mountains',
             'Tofino', 'Union Bay', 'Vuntut']
name_list = ['White Lake', 'Waterton Lakes', 'Whistler Blackcomb',
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

for index, region in enumerate(region_fake):
    print(region)
    date_offset = datetime.timedelta(weeks=index+47)
    query_fake = RegionQuery(
        region=region,
        start_date=start_date,
        end_date=end_date
    )
    fake_tweets = scraper.compile_tweets(query_fake)
    for tweet in fake_tweets:
        tweet.created_at -= date_offset
    fake_parsed_tweets: RegionQueryResult = parser.parse(query_fake, fake_tweets)
    merged_result.tweets += fake_parsed_tweets.tweets
#
# saving into pickle file
file_to_store = open("../stored_results_7.pickle", "wb")
pickle.dump(merged_result, file_to_store)
file_to_store.close()
print("Saved")

# ['Aulavik', 'Auyuittuq', 'Bruce Peninsula', 'Cape Breton Highlands', 'Elk Island','Forillon',
#              'Fort Langley', 'Fort Nelson', 'Georgian Bay Islands', 'Galiano Island', 'Gibsons', 'Gros Morne', 'Gulf Islands',
#              'Gwaii Haanas', 'Ivvavik', 'Jackson Arm', 'Kejimkujik', 'Kluane', 'Kootenay', 'Kouchibouguac', 'La Mauricie',
#              'Lake Huron', 'Lake Louise', 'Lake Superior', 'Mingan Archipelago', 'Mont-Tremblant',
#              'Mount Logan', 'Mount Revelstoke', 'Moraine Lake', "Naats'ihch'oh", 'Nahanni', 'Niagara Falls',
#              'Pacific Rim', 'Point Pelee', 'Prince Albert', 'Prince Edward Island', 'Pukaskwa', 'Quttinirpaaq',
#              'Riding Mountain', 'Sable Island', 'Sirmilik', 'Terra Nova', 'Thousand Islands', 'Torngat Mountains',
#              'Tuktut Nogait', 'Ukkusiksalik', 'Vuntut', 'Wapusk', 'Waterton Lakes', 'Whistler Blackcomb',
#              'Wood Buffalo', 'Yoho']
