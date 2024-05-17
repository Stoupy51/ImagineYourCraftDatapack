
# Generate ores in database
from user.insert_ores import *
from src.utils.database_helper import *
ores = {
	"adamantium_fragment":	EquipmentsConfig(DEFAULT_ORE.NETHERITE, 1873, {"generic.attack_damage": 0.2, "generic.armor": 0.2, "player.mining_efficiency": 0.2}),
	"sapphire":				EquipmentsConfig(DEFAULT_ORE.DIAMOND, 1752, {"player.mining_efficiency": 0.2}),
	"ruby":					EquipmentsConfig(DEFAULT_ORE.DIAMOND, 1647, {"generic.attack_damage": 0.5, "generic.armor": 0.5, "player.mining_efficiency": 0.1}),
	"topaz":				EquipmentsConfig(DEFAULT_ORE.DIAMOND, 1281, {"generic.attack_damage": 1.0, "generic.armor": 1.0}),
	"obsidian_ingot":		EquipmentsConfig(DEFAULT_ORE.DIAMOND, 3902, {"generic.attack_damage": -0.2, "player.mining_efficiency": -0.2}),
	"minecraft:emerald":	EquipmentsConfig(DEFAULT_ORE.DIAMOND, 736, {"generic.luck": 0.25}),
	"steel_ingot":			EquipmentsConfig(DEFAULT_ORE.IRON, 444, {"player.mining_efficiency": 0.1}),
	"lignite":				None,
	"slate":				None,
}
for ore, conf in ores.items():
	generate_everything_about_this_ore(DATABASE, ore, conf)

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

