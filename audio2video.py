
import sys, subprocess, os.path
from os import path

if len(sys.argv) > 1:
    title = sys.argv[1]
else:
    print("please provide the title")
    exit(-1)

os.system("mkdir -p build/" + title)
        
audioFilesPath = "../../audio/yaseen/" + title
files = os.listdir(audioFilesPath)
files.sort()
count = 0
for file in files:
    count = count + 1
    print("Processing: " + file)
    imageFile = "build/yaseen.png"
    audioFile = audioFilesPath + "/" + file
    videoFileName = "build/" + title + "/" + title + "-" + str(count).zfill(3)
    if path.exists(imageFile) and not path.exists(videoFileName + ".mp4"):
        subprocess.call(["ffmpeg", "-y", "-loop", "1", "-i", imageFile, "-i", audioFile, "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p", "-shortest", videoFileName + "~.mp4"])
        os.system("mv " + videoFileName + "~.mp4 " + videoFileName + ".mp4")
