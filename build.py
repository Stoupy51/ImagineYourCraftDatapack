
# Install required libraries
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
required = ["PIL", "OpenGL.GL", "glfw", "pygame", "smithed"]
for package in required:
	try:
		__import__(package)
	except ImportError:
		os.system(f"{sys.executable} -m pip install {package}")

# Imports
if __name__ == "__main__":
	# Get start time & Enable colors in Windows 10 console
	import time
	START_TIME = time.time()
	os.system("color")

	from config import *

	# Initialize build process
	from src.initialize import *

	# Generate items/blocks database and verify the format
	from user.database import *
	from src.verify_database import *

	# Generate manual
	if HAS_MANUAL:
		from src.manual.main import *

	# Generate resource pack
	from src.resource_pack.main import *

	# Generate datapack
	from src.datapack.main import *

	# Finalyze build process
	from src.finalyze import *

	# Total time
	total_time = time.time() - START_TIME
	info(f"Build finished in {total_time:.3f} seconds")

