from dataclasses import dataclass

from src.spaces.data.query import RegionQuery


@dataclass
class RegionActivity:
    query: RegionQuery
    activity: float
