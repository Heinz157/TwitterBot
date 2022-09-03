from pytube import YouTube, Playlist
import random

def downloadVideo():
    p = Playlist("https://www.youtube.com/playlist?list=PLheJxfe3aFemNZE60tdeu4mhCx2ExRd7I")
    playedVideos = []

    video = random.choice(p.video_urls)
    if video not in playedVideos:
        playedVideos.append(video)
        YouTube(video).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print(video)
        print()
        print(playedVideos)




