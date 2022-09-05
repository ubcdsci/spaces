import datetime
from dataclasses import dataclass


@dataclass
class Tweet:
    post_date: datetime.datetime
    tweet_text: str

    @classmethod
    def from_tweepy(cls, tweet):
        created_at = tweet.created_at
        text = tweet.text
        return cls(created_at, text)
