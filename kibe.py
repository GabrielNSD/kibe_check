from decouple import config
from tweepy import API, Cursor, OAuthHandler


class Tweet:
    def __init__(self, tweet_id):
        auth = OAuthHandler(config("CONSUMER_KEY"), config("CONSUMER_SECRET"))
        auth.set_access_token(config("ACCESS_TOKEN"), config("ACCESS_TOKEN_SECRET"))
        self.api = API(auth)
        self.data = self.api.get_status(tweet_id)
        self._duplicates = None  # cache

    @property
    def duplicates(self):
        if self._duplicates:
            return self._duplicates

        query = f"{self.data.text}  -filter:retweets"
        self._duplicates = tuple(
            tweet
            for tweet in Cursor(self.api.search, q=query).items()
            if self.is_kibe_of(tweet)
        )
        return self._duplicates

    def is_kibe_of(self, tweet):
        if self.data.id == tweet.id:
            return False

        if tweet.retweeted:
            return False

        if tweet.text.startswith("RT @{self.data.author.screen_name}"):
            return False

        return True

    @property
    def is_kibe(self):
        return bool(len(self.duplicates))

    def url(self, tweet=None):
        tweet = tweet or self.data
        return f"https://twitter.com/{tweet.author.screen_name}/status/{tweet.id}"

    def __str__(self):
        if not self.is_kibe:
            return "Not a kibe."

        return "\n".join(
            f"{count:0>2d}. {self.url(tweet)}"
            for count, tweet in enumerate(self.duplicates, 1)
        )
