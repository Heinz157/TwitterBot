## Create a twitter bot that will post a random meme from a youtube playlist every 24 hours
# - THIS IS FOR EDUCATIONAL PURPOSES ONLY
# - I DO NOT OWN ANY OF THE CONTENT IN THE PLAYLIST

# This bot randonly selects a youtube video from a playlist and posts it to twitter

1. Create a twitter account for your bot
2. Create a youtube playlist with the videos you want to post
3. Create a twitter app and get the keys
4. Create a .env file with the following keys
    - CONSUMER_KEY
    - CONSUMER_SECRET
    - ACCESS_TOKEN
    - ACCESS_TOKEN_SECRET
    - YOUTUBE_API_KEY
    - YOUTUBE_PLAYLIST_ID
5. Function to get a random video from the playlist
6. Function to download video
7. Function to post video to twitter
8. Add video to list so there are no duplicates
9. Run the bot every 24 hours

# Current issues
- The bot will post the same video twice if the playlist has less than 2 videos
- some videos do not upload correctly
- some videos are too large to post 