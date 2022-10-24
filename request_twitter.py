import tweepy
from credentials import *
import json


class AllStream(tweepy.StreamingClient):

    def on_connect(self):

        print("Connected Succesfully")

    def on_connection_error(self):
        self.disconnect()

    def on_data(self, raw_data):

        
        json_response = json.loads(raw_data)

        for key, value in json_response.items():
            print(key)
        
        # if 'location' in json_response.keys():
        #     tweet_data = [str(json_response['data']['id']),
        #               str(json_response['data']['text']),
        #               str(json_response['includes']['users'][0]['location'])]

        # print(tweet_data)

    
class StartStream():

    def __init__(self, stream):
        
        self.stream = stream

    def insert_filter(self, *filter):

        for key in filter:
            self.stream.add_rules(tweepy.StreamRule(key))

    def start_stream(self):
        self.stream.filter(expansions = "author_id", user_fields = ["location"] )


stream = AllStream(API_BEARER_TOKEN)
    
stream_data = StartStream(stream)

stream_data.insert_filter(["Lula"])

stream_data.start_stream()



    



