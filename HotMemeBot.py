import tweepy
import twitterkeys
import time
import schedule
import youtubeDownloader

## Twitter API V2.0 

client = tweepy.Client(consumer_key=twitterkeys.api_key,
                        consumer_secret=twitterkeys.api_secret,
                        access_token=twitterkeys.access_token,
                        access_token_secret=twitterkeys.access_token_secret)

def tweet():
    response = client.create_tweet(media_ids=memeMedia)
    print(response)

##Twitter API V1.1
access_token = twitterkeys.access_token
access_token_secret = twitterkeys.access_token_secret

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key=twitterkeys.api_key, consumer_secret=twitterkeys.api_secret)
 
# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
 
# calling the api
api = tweepy.API(auth)
 
# the name of the media file + Upload the media
filename = "media/meme1.mp4"
media = api.media_upload(filename)
memeMedia = [media.media_id_string]



# Timer
schedule.every().day.at("12:00").do(tweet) 

while True:
    schedule.run_pending()
    time.sleep(60)