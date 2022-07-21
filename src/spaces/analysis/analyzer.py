import os


from abc import ABC, abstractmethod

from src.spaces.data.activity import RegionActivity
from src.spaces.data.result import RegionQueryResult


class TweetAnalyzer(ABC):
    def __init__(self):
        pass

    """
    Estimate the activity of a queried region at a specified time.
    """

    @abstractmethod
    def analyze(self, result: RegionQueryResult) -> RegionActivity:
        pass
