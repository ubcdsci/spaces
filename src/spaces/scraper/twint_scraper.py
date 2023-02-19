import os

import tweepy as tw
import twint as tn
import nest_asyncio

from src.spaces.data.query import RegionQuery

from typing import List


class TwintScraper:
    def __init__(self):
        pass

    def compile_tweets(self, query: RegionQuery, save_path):
        c = tn.Config()
        c.Search = query.region
        c.Lang = "en"
        c.Since = query.start_date.strftime('%Y-%m-%d %H:%M:%S')
        c.Until = query.end_date.strftime('%Y-%m-%d %H:%M:%S')
        c.Hide_output = False
        c.Store_json = True
        c.Output = save_path
        #adjust path to somewhere temporary
        return tn.run.Search(c)


