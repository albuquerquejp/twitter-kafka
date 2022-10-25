import tweepy
from credentials import *
import json


class AllStream(tweepy.StreamingClient):

    def on_connect(self):

        print("Connected Succesfully")

    def on_connection_error(self):
        self.disconnect()

    def on_data(self, raw_data):

        # Serializing the raw data into a Json
        json_response = json.loads(raw_data)
        
        # Retrieve location data, tweet text and id. If the location does not exist, signed None
        if "location" in json_response["includes"]["users"][0]:
            
            tweet_data = {"tweeet_id":json_response["data"]["id"], "tweet_text":json_response["data"]["text"],"location":json_response["includes"]["users"][0]["location"]}
        
        else: 
            
            tweet_data = {"tweeet_id":json_response["data"]["id"], "tweet_text":json_response["data"]["text"],"location":None}
        
        return tweet_data


    

        

    
class StartStream():

    def __init__(self, stream):
        
        self.stream = stream

    # Adding a rule to search for Tweets
    def insert_filter(self, *filter):

        for key in filter:
            self.stream.add_rules(tweepy.StreamRule(key))


    # Defining which filters will be used.
    def start_stream(self):
        self.stream.filter(expansions = "author_id", user_fields = ["location"] )


stream = AllStream(API_BEARER_TOKEN)
    
stream_data = StartStream(stream)

stream_data.insert_filter(["Lula"])

stream_data.start_stream()



    



