import datetime
import tweepy as tw

from src.spaces.analysis.example_analyzer import ExampleAnalyzer
from src.spaces.data.query import RegionQuery
from src.spaces.data.region import Region
from src.spaces.data.region_type import RegionType
from src.spaces.data.result import RegionQueryResult
from src.spaces.scraper.parser import RegionParser
from src.spaces.scraper.scraper import RegionScraper

scraper = RegionScraper()
parser = RegionParser()

# parks = ["balaclava park", "camosun", "chaldecott park", "deering island park", "memorial west park", "musqueam park",
#          "pacific spirit park", "park site on blenheim", "quadra west park", "valdez park"]

regions = [
    # Placeholder values for lat/long
    Region(
        name="Balaclava Park",
        region_type=RegionType.OUTDOOR,
        latitude=-120,
        longitude=90,
        radius=0.5
    ),
    Region(
        name="Camosun",
        region_type=RegionType.OUTDOOR,
        latitude=100,
        longitude=-20,
        radius=0.2
    )
]

# Placeholders, get the tweets from yesterday to today
start_date = datetime.datetime.now() - datetime.timedelta(days=1)
end_date = datetime.datetime.now()


analyzer = ExampleAnalyzer()

results = []

for region in regions:

    query = RegionQuery(
        region=region,
        start_date=start_date,
        end_date=end_date
    )
    tweets: tw.Cursor = scraper.compile_tweets(query)
    parsed_tweets: RegionQueryResult = parser.parse(query, tweets)

    results.append(analyzer.analyze(parsed_tweets))

print(results)