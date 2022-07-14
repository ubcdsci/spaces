from dataclasses import dataclass

import tweepy as tw

from src.spaces.data.query import RegionQuery

@dataclass
class RegionQueryResult:
    query: RegionQuery
    tweets: tw.Cursor
