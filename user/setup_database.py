
# Import database helper
from python_datapack.utils.database_helper import *

# Imports
from .additions import main as additions_main
from .custom_blocks import main as custom_blocks_main

# Constants
STARTING_CMD: int = 2015000	# Prefix for custom_model_data
ORES_CONFIGS: dict[str, EquipmentsConfig|None] = {
	"adamantium_fragment":	EquipmentsConfig(DEFAULT_ORE.NETHERITE, 1873, {"generic.attack_damage": 0.2, "generic.armor": 0.2, "player.mining_efficiency": 0.2}),
	"sapphire":				EquipmentsConfig(DEFAULT_ORE.DIAMOND, 1752, {"player.mining_efficiency": 0.2}),
	"ruby":					EquipmentsConfig(DEFAULT_ORE.DIAMOND, 1647, {"generic.attack_damage": 0.5, "generic.armor": 0.5, "player.mining_efficiency": 0.1}),
	"topaz":				EquipmentsConfig(DEFAULT_ORE.DIAMOND, 1281, {"generic.attack_damage": 1.0, "generic.armor": 1.0}),
	"obsidian_ingot":		EquipmentsConfig(DEFAULT_ORE.DIAMOND, 3902, {"generic.attack_damage": -0.2, "player.mining_efficiency": -0.2}),
	"minecraft:emerald":	EquipmentsConfig(DEFAULT_ORE.DIAMOND, 736, {"generic.luck": 0.25}),
	"steel_ingot":			EquipmentsConfig(DEFAULT_ORE.IRON, 444, {"player.mining_efficiency": 0.1}),
	"lignite":				None,
	"slate":				None,
	"minecraft:stone":		None,
}

# Main function should return a database
def main(config: dict) -> dict[str, dict]:
	database = {}

	# Generate ores in database
	generate_everything_about_these_materials(config, database, ORES_CONFIGS)

	# Apply database additions
	database = additions_main(database)

	# Add custom blocks vanilla block
	custom_blocks_main(database)

	# Add custom records
	generate_custom_records(config, database, "auto")

	# Final adjustments
	deterministic_custom_model_data(config, database, STARTING_CMD)
	add_item_name_and_lore_if_missing(config, database)
	add_private_custom_data_for_namespace(config, database)
	add_smithed_ignore_vanilla_behaviours_convention(database)
	print()

	# Return database
	return database

