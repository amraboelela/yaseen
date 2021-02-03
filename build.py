
import sys, subprocess, os.path
from os import path

yaseenDirectories = "../../audio/yaseen"
directories = os.listdir(yaseenDirectories)
directories.sort()
for directory in directories:
    if directory != "Bukhari":
        subprocess.call(["python3", "audio2video.py", directory])
