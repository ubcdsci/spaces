import tweepy as tw

from src.spaces.data.query import RegionQuery


class RegionScraper:
    def __init__(self):
        pass

    def compile_tweets(self, query: RegionQuery) -> tw.Cursor:
        return tw.Cursor(...)
