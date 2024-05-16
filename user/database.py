
# Generate ores in database
from user.insert_ores import *

# Add more information for each type of ore
from user.ores_properties import *

# Apply database additions
from user.additions import *

# Add custom records
from user.records import *

# Add custom blocks vanilla block
from user.custom_blocks import *

# For every key, apply common data and remove unused keys
from user.final_adjustments import *

# Print not used textures and a bit of the database keys, then dump the database to a JSON file
from user.debug import *
print()

