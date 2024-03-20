
# Generate ores in database
from database.insert_ores import *

# Apply database additions
from database.additions import *

# For every key, apply common data and remove unused keys
from database.final_adjustments import *

# Print not used textures and a bit of the database keys, then dump the database to a JSON file
from database.debug import *

