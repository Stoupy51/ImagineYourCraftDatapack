
# Install required libraries
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
required = ["imageio", "PIL", "OpenGL.GL", "glfw", "pygame"]
for package in required:
	try:
		__import__(package)
	except ImportError:
		os.system(f"pip install {package}")

# Additional imports
from PIL import Image, ImageEnhance
import requests
import imageio
import shutil
import math
import time
import json
import io

# Import all
from src.config import *
from src.utils import *

