import os

import tweepy as tw

from src.spaces.data.query import RegionQuery


class RegionScraper:
    def __init__(self):
        try:
            consumer_key = os.getenv('SPACES_CONSUMER_KEY')
            consumer_secret = os.getenv('SPACES_CONSUMER_SECRET')
            access_token = os.getenv('SPACES_ACCESS_TOKEN')
            access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
            # consumer_key = 'hosqIjsByqmOUkq4XHnfd04pd'
            # consumer_secret = 'H7oKCjJib4ysDsOBZKEK4KKDMYaI53Da5ZA0peV6Q914a1NNOs'
            # access_token = '1479208979934760963-NVEBQWtCwLaGc0lks8ijP300GbzWb4'
            # access_token_secret = 'W7FmZGYEI3gWXhujWFaP0BJwtkOR6xfZOaOoB2AcOAwqW'
        except KeyError as e:
            print("Your environment variables do not contain the necessary API keys for tweepy.")
            raise e

        for key, value in os.environ.items():
            print('{}:{}'.format(key, value))

        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tw.API(auth, wait_on_rate_limit=True)
        # probably not finished and needs some more work

    def compile_tweets(self, query: RegionQuery) -> tw.Cursor:
        # Take the information from RegionQuery and pass it into the tw.Cursor object
        # for tweet in tw.Cursor(self.api.search_tweets, query).items():
        return tw.Cursor(self.api.search_tweets, query).items()

# REFERENCE:
#
#
#
#
# import os
# import tweepy as tw
# import pandas as pd
# from pandas import ExcelWriter
#
# auth = tw.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tw.API(auth, wait_on_rate_limit=True)
#
# search_words = "balaclava park"
#
# tweet_sandbox = pd.DataFrame(columns=['Tweet_Id', 'Tweet_Date', 'Tweet_Text'])
#
# for tweet in tw.Cursor(api.search_full_archive, label="twitterpull",
#                        query=search_words, fromDate=202103150000,
#                        toDate=202103310000).items():
