import tweepy
from kafka import KafkaProducer
from twitter_credentials import *
from kafka_credentials import *
from aws_credentials import *
import boto3
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

        # Sending the tweet data using a kafka producer. 
        producer_1.send('tweets', json.dumps(tweet_data).encode('utf-8'))

        # Conducting a sentiment analysis, through boto3 and Amazon Comprehend.
        comprehend = boto3.client(service_name = 'comprehend', region_name='us-east-2', aws_access_key_id= ACCESS_KEY, aws_secret_access_key= SECRET_ACCESS_KEY)
        
        # For sentiment analysis it is only necessary to pass the text of the tweets
        response = comprehend.detect_sentiment(Text=tweet_data["tweet_text"], LanguageCode='pt')

        sentiment_result = {"Sentiment":response["Sentiment"], "SentimentScore":response["SentimentScore"]}
        # Sending the sentiment result data using a kafka producer.
        producer_2.send('sentiment_results', json.dumps(sentiment_result).encode('utf-8'))

class StartStream():

    def __init__(self, stream):
        
        self.stream = stream

    # Adding a rule to search for Tweets
    def insert_filter(self, *args):

        for key in args:
            self.stream.add_rules(tweepy.StreamRule(key))

    # Defining which filters will be used.
    def start_stream(self):
        self.stream.filter(expansions = "author_id", user_fields = ["location"])

producer_1 = KafkaProducer(sasl_plain_username=USERNAME, sasl_plain_password=PASSWORD, sasl_mechanism=MECHANISM, security_protocol=PROTOCOL, bootstrap_servers= SERVERS)

producer_2 = KafkaProducer(sasl_plain_username=USERNAME_2, sasl_plain_password=PASSWORD_2, sasl_mechanism=MECHANISM, security_protocol=PROTOCOL, bootstrap_servers= SERVERS)

stream = AllStream(API_BEARER_TOKEN)
    
stream_data = StartStream(stream)

# Keys to be searched 
stream_data.insert_filter(["Lula","Bolsonaro"])

stream_data.start_stream()




    



