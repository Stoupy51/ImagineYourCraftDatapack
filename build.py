
# Install required libraries
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
required = ["PIL", "OpenGL.GL", "glfw", "pygame"]
for package in required:
	try:
		__import__(package)
	except ImportError:
		os.system(f"pip install {package}")

# Imports
if __name__ == "__main__":
	# Get start time & Enable colors in Windows 10 console
	import time
	START_TIME = time.time()
	os.system("color")

	from src.importer import *

	# Initialize build process
	from src.initialize import *

	# Generate items/blocks database
	from database.main import *

	# Generate manual
	from src.manual.main import *

	# Generate resource pack
	from src.resource_pack.main import *

	# Generate datapack
	from src.datapack.main import *

	# Finalyze build process
	from src.finalyze import *
	src_finalyze()

	# Total time
	total_time = time.time() - START_TIME
	info(f"Build finished in {total_time:.3f} seconds")

