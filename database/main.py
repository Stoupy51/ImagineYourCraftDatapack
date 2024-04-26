
# Generate ores in database
from database.insert_ores import *

# Add more information for each type of ore
from database.ores_properties import *

# Apply database additions
from database.additions import *

# Add custom records
from database.records import *

# Add custom blocks vanilla block
from database.custom_blocks import *

# For every key, apply common data and remove unused keys
from database.final_adjustments import *

# Print not used textures and a bit of the database keys, then dump the database to a JSON file
from database.debug import *
print()

