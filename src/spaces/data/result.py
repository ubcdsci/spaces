import collections
import datetime
from dataclasses import dataclass
from typing import List

import tweepy as tw

from src.spaces.data.query import RegionQuery
from src.spaces.data.tweet import Tweet


@dataclass
class RegionQueryResult:
    query: RegionQuery
    tweets: List[Tweet]


