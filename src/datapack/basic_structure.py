
# Imports
from src.config import *
from src.utils.io import *
from src.utils.print import *

# Tick structure, tick_2 and second_5 are "offsync" for a better load distribution
write_to_file(f"{DATAPACK_FUNCTIONS}/tick.mcfunction", f"""
# Timers
scoreboard players add #tick_2 {NAMESPACE}.data 1
scoreboard players add #second {NAMESPACE}.data 1
scoreboard players add #second_5 {NAMESPACE}.data 1
scoreboard players add #minute {NAMESPACE}.data 1
execute if score #tick_2 {NAMESPACE}.data matches 3.. run function {NAMESPACE}:tick_2
execute if score #second {NAMESPACE}.data matches 20.. run function {NAMESPACE}:second
execute if score #second_5 {NAMESPACE}.data matches 90.. run function {NAMESPACE}:second_5
execute if score #minute {NAMESPACE}.data matches 1200.. run function {NAMESPACE}:minute
""")

# Write remaining files
write_to_file(f"{DATAPACK_FUNCTIONS}/tick_2.mcfunction", f"""
# Reset timer
scoreboard players set #tick_2 {NAMESPACE}.data 1
""")
write_to_file(f"{DATAPACK_FUNCTIONS}/second.mcfunction", f"""
# Reset timer
scoreboard players set #second {NAMESPACE}.data 0
""")
write_to_file(f"{DATAPACK_FUNCTIONS}/second_5.mcfunction", f"""
# Reset timer
scoreboard players set #second_5 {NAMESPACE}.data -10
""")
write_to_file(f"{DATAPACK_FUNCTIONS}/minute.mcfunction", f"""
# Reset timer
scoreboard players set #minute {NAMESPACE}.data 1
""")


