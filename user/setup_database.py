
# Imports and constant
from src.importer import *
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
	"minecraft:stone":		None,
}
generate_everything_about_these_ores(DATABASE, ores_configs)

# Apply database additions
from user.additions import *

# Add custom blocks vanilla block
from user.custom_blocks import *

# Add custom records
records = {
	"record_1":		("AntVenom - The Miner.ogg", 252.0),
	"record_2":		("BebopVox - Don't Mine At Night.ogg", 228.0),
	"record_3":		("CaptainSparklez - Fallen Kingdom.ogg", 287.0),
	"record_4":		("CaptainSparklez - Minecraft Style.ogg", 237.0),
	"record_5":		("CaptainSparklez - Revenge.ogg", 264.0),
	"record_6":		("CaptainSparklez - Tack Back the Night.ogg", 390.0),
	"record_7":		("CaptainSparklez - TNT.ogg", 204.0),
	"record_8":		("Gunther - You touch my tralala.ogg", 240.0),
	"record_9":		("GuzzProduction - Bouge Ton Cube.ogg", 151.0),
	"record_10":	("Lokoise - ACTA.ogg", 200.0),
	"record_11":	("Lokoise - Bug de chunks.ogg", 233.0),
	"record_12":	("Lokoise - J'aime le creep'.ogg", 199.0),
	"record_13":	("Lokoise - Je me give.ogg", 209.0),
	"record_14":	("Lokoise - J'fais des pelles en diam's.ogg", 209.0),
	"record_15":	("Lokoise - J'geek un max.ogg", 124.0),
	"record_16":	("Lokoise - J'suis Sean Kévin.ogg", 227.0),
	"record_17":	("Lokoise - Le journal d'un naufragay.ogg", 95.0),
	"record_18":	("Lokoise - Tous les zombies.ogg", 204.0),
	"record_19":	("Lokoise - Un débit tout pourri.ogg", 200.0),
	"record_20":	("ReAperr & MrElvilia - Mauvaise Idée.ogg", 191.0),
	"record_21":	("TheDudesCraft - GAGAOUTAI.ogg", 234.0),
	"record_22":	("TryHardNinja - That Girl is Crafty.ogg", 236.0),
}
generate_custom_records(DATABASE, records)

# Final adjustments
deterministic_custom_model_data(DATABASE, STARTING_CMD)
clean_up_empty_recipes(DATABASE)
add_item_name_and_lore_if_missing(DATABASE)
add_private_custom_data_for_namespace(DATABASE)
add_smithed_ignore_vanilla_behaviours_convention(DATABASE)
print()

