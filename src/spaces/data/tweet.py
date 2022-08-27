import datetime
from dataclasses import dataclass


@dataclass
class Tweet:
    post_date: datetime.datetime
    text: str

    @classmethod
    def from_tweepy(cls, tweet):
        created_at = tweet.created_at
        text = tweet.full_text
        return cls(created_at, text)
