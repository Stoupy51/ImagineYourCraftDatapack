
# Install required libraries
import os
required = ["imageio"]
for package in required:
	try:
		__import__(package)
	except ImportError:
		os.system(f"pip install {package}")

# Additional imports
import imageio
import shutil
import json
import io

# Import all
from src.config import *
from src.utils import *

