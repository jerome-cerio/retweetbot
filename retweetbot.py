# This Python project accesses the Twitter API v2 to
# retweet tweets from Rice University and Rice Engineering
# that contain the words "engineering", "engineer", and "computer science"

import tweepy

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key="BRk26MYooLHEzoYYwOqLDzbX6",
    consumer_secret="DJzXnMLjfFQtq8kWnydzm1zzKZ7EeCUOQ36vyH6b7Swr2bZsQY",
    access_token="1340499997645803520-jobo7LM7po9n90T4csrkSOoqIz9tVW",
    access_token_secret="rmtKHy5cA0pUei83slho17cD1Z4MxA1uu9jVjZXoMaAnx"
)

# Create API object to constantly stream tweets

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

        try:
            client.retweet(tweet.id)
        except Exception as error:
            print(error)

# Create a stream
stream = MyStream(bearer_token= "AAAAAAAAAAAAAAAAAAAAABrApwEAAAAAh%2FcAWKELOQxFvV7DbAxJMHOAXhc%3Diy4YWulSIWvjvrvSXrbZHb2Y2mFUaEsUSDBV3FLIai4B7UMyDI")

# Specify which accounts to retweet
target1 = client.get_user(username = "RiceUniversity").data.id
target2 = client.get_user(username = "RiceEngineering").data.id

# Specify rules for which tweets to retweet. Keywords: Rice engineering
rule = tweepy.StreamRule("(engineering)(engineers)(computer science)(-is:reply -is:retweet)", user_ids = [target1, target2])

stream.add_rules(rule)

# Start streaming
stream.filter()