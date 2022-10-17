import tweepy
from credentials import *

client = tweepy.Client(API_BEARER_TOKEN, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


filters = ["Lula", "Bolsonaro"]


class AllStream(tweepy.StreamingClient):

    def on_connect(self):

        print("Connected")

        return True

    def on_tweet(self, tweet):


        if tweet.referenced_tweets == None:
            print(tweet.text)
            client.like(tweet.id)

            time.sleep(10)

stream = AllStream(bearer_token=API_BEARER_TOKEN)

for term in filters:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])


    