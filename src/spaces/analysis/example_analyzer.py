import random

from src.spaces.analysis.analyzer import TweetAnalyzer
from src.spaces.data.activity import RegionActivity
from src.spaces.data.result import RegionQueryResult

"""
Example analyzer to estimate the activity in a specific region. Produces a random number for the requested region
"""


class ExampleAnalyzer(TweetAnalyzer):
    def analyze(self, result: RegionQueryResult) -> RegionActivity:
        return RegionActivity(
            query=result.query,
            activity=random.random()
        )
