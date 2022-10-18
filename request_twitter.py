import tweepy
from credentials import *


class AllStream(tweepy.StreamingClient):

    def on_connect(self):

        print("Connected Succesfully")

    def on_connection_error(self):
        self.disconnect()

    def on_data(self, raw_data):

        print(raw_data)

    def on_status(self, status):

        print ("Tweet Text: ",status.text)



stream_data = AllStream(API_BEARER_TOKEN)

filter = ["Lula", "Bolsonaro"]

for key in filter:
    stream_data.add_rules(tweepy.StreamRule(key))

stream_data.filter(tweet_fields=["referenced_tweets"])
    



