import tweepy as tw

from src.spaces.data.query import RegionQuery
from src.spaces.data.result import RegionQueryResult


class RegionParser:
    def __init__(self):
        pass

    def parse(self, query: RegionQuery, tweets: tw.Cursor) -> RegionQueryResult:
        # Parsing method TBD
        return RegionQueryResult(
            query=query,
            tweets=tweets
        )

