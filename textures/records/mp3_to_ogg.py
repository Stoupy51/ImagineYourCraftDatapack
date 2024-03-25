
# Script that converts all mp3 files in the current directory to ogg files.
# Requires ffmpeg to be installed.

import os
import subprocess

for file in os.listdir("."):
	if file.endswith(".mp3"):
		src = file
		dst = file.replace(".mp3", ".ogg")
		subprocess.run(["ffmpeg", "-i", src, dst])
	pass
print("Conversion finished!")

