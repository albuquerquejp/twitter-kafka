# Twitter Data Stream

Project for analyzing data retrieved from the twitter API, through a data stream. The tweets will be retrieved using Tweepy (Python Library) and, later, after processing these records, the data must be uploaded to a cloud database for further analysis.



![Tweet Sentiment Analysis](https://user-images.githubusercontent.com/101363298/199965181-6849a5c9-554b-4b05-93fd-53659f2bc9c9.jpeg)

<sup>ETL Diagram</sup>

For this project, I wanted to understand how was the sentiment of the tweets about the 2 candidates of Brazil's 2022 Presidential Runoff. For this, the following technologies were used:
- **Twitter API**, for real-time data retrieval.
- **Tweepy**, Python library for communicating with the Twitter API
- **Amazon Comprehend (boto3)**, used to perform sentiment analysis of retrieved tweets.
- **Kafka**, both retrieved tweets and sentiment analysis were sent as messages by a producer to a cluster in the cloud (Confluent Cloud).![Topics](https://user-images.githubusercontent.com/101363298/199969244-d5030d7b-8f5a-4730-b7e2-9ef349a792ad.png)
- **S3 Bucket**, using Sink Connectors, messages sent to Kafka were stored in real time in an S3 Bucket.![s3_sentiment](https://user-images.githubusercontent.com/101363298/199969050-5e393329-753f-4db1-ba3a-ec03aec3dc0c.png)
- With both the tweets and the sentiment analysis results stored in a Bucket, **AWS Glue Crawler** and **Amazon Athena** were used to transform this data, stored in Json, so that it was possible to visualize the results in **Amazon QuickSight**.![Athena Table](https://user-images.githubusercontent.com/101363298/199968863-1079570c-6663-45a6-a35d-f018dd1a7846.png)

**Sentiment Analysis Result:**

![Sentiment result](https://user-images.githubusercontent.com/101363298/199969680-a7752b7a-56e9-4963-bbaf-7729671643ff.png)
