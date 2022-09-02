import tweepy
import twitterkeys



client = tweepy.Client(consumer_key=twitterkeys.api_key,
                        consumer_secret=twitterkeys.api_secret,
                        access_token=twitterkeys.access_token,
                        access_token_secret=twitterkeys.access_token_secret)

response = client.create_tweet(text = "Hello, world!")
print(response)


