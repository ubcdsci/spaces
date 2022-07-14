import datetime
from dataclasses import dataclass

from src.spaces.data.region import Region


@dataclass
class RegionQuery:
    region: Region
    start_date: datetime.datetime
    end_date: datetime.datetime
    # More query options here
