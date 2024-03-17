
# Install required library
try:
	import imageio
except ImportError:
	import os
	os.system("pip install imageio")

# Import all
from src.config import *
from src.utils import *

