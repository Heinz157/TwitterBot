import os

# put all the files in the directory in a list then return the .mp4 file
def getVideo():
    files = os.listdir()
    for file in files:
        if file.endswith(".mp4"):
            memeVideo = file
            return memeVideo