
import sys, subprocess, os.path
from os import path

if len(sys.argv) > 1:
    title = sys.argv[1]
else:
    print("please provide the title")
    exit(-1)

audioFilesPath = "../../audio/yaseen/" + title
files = os.listdir(audioFilesPath)
files.sort()
for file in files:
    fileSplit = file.split(".")
    fileName = fileSplit[0]
    print("Generating: " + fileName)
    imageFile = "build/yaseen.png"
    audioFile = audioFilesPath + "/" + file
    videoFile = "build/" + title + "/" + title + "-" + fileName + ".mp4"
    subprocess.call(["ffmpeg", "-y", "-loop", "1", "-i", imageFile, "-i", audioFile, "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p", "-shortest", videoFile])
