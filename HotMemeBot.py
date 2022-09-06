import tweepy
import twitterkeys
import time
import schedule
import youtubeDownloader
import os



def tweet():
    # Checks if there is a video in the directory
    if os.path.exists("meme.mp4"):
        os.remove("meme.mp4")

    # Download the video
    youtubeDownloader.downloadVideo()
    # wait for the video to download
    time.sleep(1)
    print('Video Downloaded')
    print()

    # get the video file
    files = os.listdir()
    for file in files:
        if file.endswith(".mp4"):
            print('File Found: ' + file)
            print()

            # rename file to meme.mp4
            os.rename(file, 'meme.mp4')
            print('File Renamed')
            print()


    # the name of the media file + Upload the media
    media = api.media_upload('meme.mp4')
    memeMedia = [media.media_id_string]
    print(memeMedia)

    # Post the tweet with the media
    response = client.create_tweet(media_ids=memeMedia)
    print(response)
    print()

    # Delete the video file
    os.remove('meme.mp4')
    print('Video Deleted')





## Twitter API V2.0 

client = tweepy.Client(consumer_key=twitterkeys.api_key,
                        consumer_secret=twitterkeys.api_secret,
                        access_token=twitterkeys.access_token,
                        access_token_secret=twitterkeys.access_token_secret)

##Twitter API V1.1
access_token = twitterkeys.access_token
access_token_secret = twitterkeys.access_token_secret

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key=twitterkeys.api_key, consumer_secret=twitterkeys.api_secret)
 
# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
 
# calling the api
api = tweepy.API(auth)




# Timer
schedule.every().day.at("12:00").do(tweet) 

while True:
    schedule.run_pending()
    time.sleep(60)


