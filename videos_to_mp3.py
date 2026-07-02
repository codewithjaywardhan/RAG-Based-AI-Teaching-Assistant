import os
import subprocess


videos = os.listdir("videos")


for video in videos:
    number = video.split(" [")[0].split(" #")[1]
    title = video.split(" ｜ ")[0]

    subprocess.run(["ffmpeg","-i",f"videos/{video}",f"audios_new/{number}_{title}.mp3"])
