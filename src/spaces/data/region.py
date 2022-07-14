from dataclasses import dataclass

from src.spaces.data.region_type import RegionType


@dataclass
class Region:
    name: str
    region_type: RegionType

    # Eventually we may want to change this to be a more complex shape than a circle
    latitude: float
    longitude: float
    # Radius in metres
    radius: float
