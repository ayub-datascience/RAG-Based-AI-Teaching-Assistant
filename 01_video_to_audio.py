# Converts the videos (mp4) to audios (mp3) and save them in the "audios" folder.
import os
import subprocess

files = os.listdir("videos")
for file in files:
    tutorial_number = file.split("Tutorial #")[1].split(" - ")[0]
    file_name = file.split("  ")[0]
    print(tutorial_number, file_name)
    # Convert the video to audio using ffmpeg software and save it in the "audios" folder with the file name as: {tutorial_number}_{file_name}.mp3
    # Note: Create "audios" folder manually before running this code, otherwise it will give an error.
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
    # "-i" tells ffmpeg, this is the input file you should process it. {file}
    # f"videos/{file}" -> videos is the folder, which contains the video files and we are iterating those files using "file" variable.
    

