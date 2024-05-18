
# Imports and constant
from config import *
from src.utils.database_helper import *
STARTING_CMD = 2015000	# Prefix for custom_model_data

# Generate ores in database
ores_configs = {
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
generate_everything_about_these_ores(DATABASE, ores_configs)

# Apply database additions
from user.additions import *

# Add custom records
from user.records import *

# Add custom blocks vanilla block
from user.custom_blocks import *

# Apply deterministic custom_model_data using cache
deterministic_custom_model_data(DATABASE, STARTING_CMD)

# Final adjustments
clean_up_empty_recipes(DATABASE)
add_item_name_and_lore_if_missing(DATABASE)
add_private_custom_data_for_namespace(DATABASE)
add_smithed_ignore_vanilla_behaviours_convention(DATABASE)
print()

