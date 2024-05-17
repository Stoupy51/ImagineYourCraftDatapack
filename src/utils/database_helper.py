
# Imports
from config import *
from src.utils.ingredients import *
from src.utils.print import *
from enum import Enum
from PIL import Image

# Constants
SLOTS = {"helmet": "head", "chestplate": "chest", "leggings": "legs", "boots": "feet", "sword": "mainhand", "pickaxe": "mainhand", "axe": "mainhand", "shovel": "mainhand", "hoe": "mainhand"}
class DEFAULT_ORE(Enum):
	NETHERITE = "netherite"
	DIAMOND = "diamond"
	IRON = "iron"
	GOLD = "gold"
	CHAINMAIL = "chainmail_and_stone"	# stone tools
	LEATHER = "leather_and_wood"		# wood tools
class VanillaEquipments(Enum):
	""" Default vanilla equipments values (durability, armor, armor_toughness, knockback_resistance, attack_damage, attack_speed) """
	HELMET			= {	DEFAULT_ORE.LEATHER:	{"durability": 55,		"armor": 1},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 165,		"armor": 2},
						DEFAULT_ORE.IRON:		{"durability": 165,		"armor": 2},
						DEFAULT_ORE.GOLD:		{"durability": 77,		"armor": 2},
						DEFAULT_ORE.DIAMOND:	{"durability": 363,		"armor": 3,	"armor_toughness": 2},
			 			DEFAULT_ORE.NETHERITE:	{"durability": 407,		"armor": 3,	"armor_toughness": 3,	"knockback_resistance": 0.1}
					}
	CHESTPLATE		= {	DEFAULT_ORE.LEATHER:	{"durability": 80,		"armor": 3},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 240,		"armor": 5},
						DEFAULT_ORE.IRON:		{"durability": 240,		"armor": 6},
						DEFAULT_ORE.GOLD:		{"durability": 112,		"armor": 5},
						DEFAULT_ORE.DIAMOND: 	{"durability": 528,		"armor": 8,	"armor_toughness": 2},
						DEFAULT_ORE.NETHERITE:	{"durability": 592,		"armor": 8,	"armor_toughness": 3,	"knockback_resistance": 0.1}
					}
	LEGGINGS		= {	DEFAULT_ORE.LEATHER:	{"durability": 75,		"armor": 2},
  						DEFAULT_ORE.CHAINMAIL:	{"durability": 225,		"armor": 4},
						DEFAULT_ORE.IRON:		{"durability": 225,		"armor": 5},
						DEFAULT_ORE.GOLD:		{"durability": 105,		"armor": 3},
						DEFAULT_ORE.DIAMOND:	{"durability": 495,		"armor": 6,	"armor_toughness": 2},
						DEFAULT_ORE.NETHERITE:	{"durability": 555,		"armor": 6,	"armor_toughness": 3,	"knockback_resistance": 0.1}
					}
	BOOTS			= {	DEFAULT_ORE.LEATHER:	{"durability": 65,		"armor": 1},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 195,		"armor": 1},
						DEFAULT_ORE.IRON:		{"durability": 195,		"armor": 2},
						DEFAULT_ORE.GOLD:		{"durability": 95,		"armor": 1},
						DEFAULT_ORE.DIAMOND:	{"durability": 429,		"armor": 3,	"armor_toughness": 2},
						DEFAULT_ORE.NETHERITE:	{"durability": 481,		"armor": 3,	"armor_toughness": 3,	"knockback_resistance": 0.1}
					}
	SWORD			= {	DEFAULT_ORE.LEATHER:	{"durability": 59,		"attack_damage": 4,		"attack_speed": -2.50},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 131,		"attack_damage": 5,		"attack_speed": -2.50},
						DEFAULT_ORE.IRON:		{"durability": 250,		"attack_damage": 6,		"attack_speed": -2.50},
						DEFAULT_ORE.GOLD:		{"durability": 32,		"attack_damage": 4,		"attack_speed": -2.50},
						DEFAULT_ORE.DIAMOND:	{"durability": 1561,	"attack_damage": 7,		"attack_speed": -2.50},
						DEFAULT_ORE.NETHERITE:	{"durability": 2031,	"attack_damage": 8,		"attack_speed": -2.50}
					}
	PICKAXE			= {	DEFAULT_ORE.LEATHER:	{"durability": 59,		"attack_damage": 2,		"attack_speed": -2.75},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 131,		"attack_damage": 3,		"attack_speed": -2.75},
						DEFAULT_ORE.IRON:		{"durability": 250,		"attack_damage": 4,		"attack_speed": -2.75},
						DEFAULT_ORE.GOLD:		{"durability": 32,		"attack_damage": 2,		"attack_speed": -2.75},
						DEFAULT_ORE.DIAMOND:	{"durability": 1561,	"attack_damage": 5,		"attack_speed": -2.75},
						DEFAULT_ORE.NETHERITE:	{"durability": 2031,	"attack_damage": 6,		"attack_speed": -2.75}
					}
	AXE				= {	DEFAULT_ORE.LEATHER:	{"durability": 59,		"attack_damage": 7,		"attack_speed": -3.20},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 131,		"attack_damage": 9,		"attack_speed": -3.20},
						DEFAULT_ORE.IRON:		{"durability": 250,		"attack_damage": 9,		"attack_speed": -3.10},
						DEFAULT_ORE.GOLD:		{"durability": 32,		"attack_damage": 7,		"attack_speed": -3.00},
						DEFAULT_ORE.DIAMOND:	{"durability": 1561,	"attack_damage": 9,		"attack_speed": -3.00},
						DEFAULT_ORE.NETHERITE:	{"durability": 2031,	"attack_damage": 10,	"attack_speed": -3.00}
					}
	SHOVEL			= {	DEFAULT_ORE.LEATHER:	{"durability": 59,		"attack_damage": 2.5,	"attack_speed": -3.20},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 131,		"attack_damage": 3.5,	"attack_speed": -3.20},
						DEFAULT_ORE.IRON:		{"durability": 250,		"attack_damage": 4.5,	"attack_speed": -3.10},
						DEFAULT_ORE.GOLD:		{"durability": 32,		"attack_damage": 2.5,	"attack_speed": -3.00},
						DEFAULT_ORE.DIAMOND:	{"durability": 1561,	"attack_damage": 5.5,	"attack_speed": -3.00},
			 			DEFAULT_ORE.NETHERITE:	{"durability": 2031,	"attack_damage": 6.5,	"attack_speed": -3.00}
					}
	HOE				= {	DEFAULT_ORE.LEATHER:	{"durability": 59,		"attack_damage": 1,		"attack_speed": -3.00},
						DEFAULT_ORE.CHAINMAIL:	{"durability": 131,		"attack_damage": 1,		"attack_speed": -2.00},
						DEFAULT_ORE.IRON:		{"durability": 250,		"attack_damage": 1,		"attack_speed": -1.00},
						DEFAULT_ORE.GOLD:		{"durability": 32,		"attack_damage": 1,		"attack_speed": -3.00},
						DEFAULT_ORE.DIAMOND:	{"durability": 1561,	"attack_damage": 1,		"attack_speed": 0},
						DEFAULT_ORE.NETHERITE:	{"durability": 2031,	"attack_damage": 1,		"attack_speed": 0}
					}
class EquipmentsConfig():
	def __init__(self, equivalent_to: DEFAULT_ORE = DEFAULT_ORE.DIAMOND, pickaxe_durability: int = 1561, attributes: dict[str, float] = {}):
		""" Creates a configuration for equipments (based on the pickaxe)
		Args:
			equivalent_to (DEFAULT_ORE):	The equivalent ore to compare to (ex: DEFAULT_ORE.DIAMOND)
			pickaxe_durability (int):		The pickaxe durability that will be used to calculate the durability of other equipments
			attributes (dict[str, float]):	(optional) Attributes with type "add_value" to add (not override) to the equipment (ex: "generic.attack_damage": 1.0, means 6 attack damage for diamond pickaxe)
				{"generic.attack_damage": 1.0, "generic.armor": 1.0, "player.mining_efficiency": 0.1}
				generic.attack_damage and player.mining_efficiency are always on tools
				generic.armor and generic.armor_toughness is always on armor
		If you need a specific attribute for a generated item, you should append it afterward.
		"""
		self.equivalent_to = equivalent_to
		self.pickaxe_durability = pickaxe_durability
		self.attributes = attributes
	def getter(self) -> tuple[DEFAULT_ORE, int, dict[str, float]]:
		return self.equivalent_to, self.pickaxe_durability, self.attributes
	def get_tools_attributes(self) -> dict[str, float]:
		NOT_ON_TOOLS = ["generic.armor", "generic.armor_toughness"]
		return {key: value for key, value in self.attributes.items() if key not in NOT_ON_TOOLS}
	def get_armor_attributes(self) -> dict[str, float]:
		NOT_ON_ARMOR = ["generic.attack_damage", "player.mining_efficiency"]
		return {key: value for key, value in self.attributes.items() if key not in NOT_ON_ARMOR}

# Generate everything related to the ore
def generate_everything_about_this_ore(database: dict[str, dict], material: str = "adamantium_fragment", equipments_config: EquipmentsConfig|None = EquipmentsConfig(DEFAULT_ORE.NETHERITE, 1873, {"attack_damage": 1.2, "player.mining_efficiency": 0.2})):
	""" Generate everything related to the ore (armor, tools, weapons, ore, and ingredients (raw, nuggets, blocks)).
		The function will try to find textures in the assets folder to each item
		And return a list of generated items if you want to do something with it.
	Args:
		database			(dict[str, dict]):		The database to update
		material			(str):					The ore/material to generate everything about (ex: "adamantium_fragment", "steel_ingot", "minecraft:emerald", "minecraft:copper_ingot")
		equipments_config	(EquipmentsConfig):	The base multiplier to apply
	Returns:
		list[str]:		The list of generated items (ex: ["adamantium_helmet", "raw_adamantium", "adamantium_block", ...])
	"""
	# Constants
	material_base = material.split(":")[-1].split("_")[0]	# Get the base material name (ex: "adamantium" from "adamantium_fragment")
	is_vanilla_material = ':' in material					# Check if the material is a vanilla material (ex: "minecraft:..." is a vanilla material)
	equivalent_to, pickaxe_durability, attributes = equipments_config.getter()	# Get the equivalent material, pickaxe durability, and attributes
	main_ingredient = ingr_repr(material)					# Get the main ingredient for recipes

	# Get ore color (for armor dye and other stuff)
	color = None
	if f"{material}_chestplate.png" in TEXTURES_FILES:
		color = Image.open(f"{ASSETS_FOLDER}/{material}_chestplate.png")
		color = list(color.getdata())										# Get image (1D Array)
		color = [(r,g,b) for (r,g,b,a) in color if a > 0]					# Get all colors that are not transparent
		color = [sum(x) / len(color) for x in zip(*color)]					# Get the average color
		color = int(color[0]) << 16 | int(color[1]) << 8 | int(color[2])	# Convert to int (Minecraft format: Red<<16 + Green<<8 + Blue)

	warning(f"material: {material}")
	warning(f"material_base: {material_base}")
	warning(f"is_vanilla_material: {is_vanilla_material}")
	warning(f"equipments_config.equivalent_to: {equivalent_to}")
	warning(f"equipments_config.pickaxe_durability: {pickaxe_durability}")
	warning(f"equipments_config.attributes: {attributes}")
	warning(f"main_ingredient: {main_ingredient}")

	# Placeables (ore, block, raw_block)
	for block in [f"{material_base}_ore", f"{material_base}_block", f"raw_{material_base}_block"]:
		if block + ".png" not in TEXTURES_FILES:
			continue
		if block not in database:
			database[block] = {}
		warning(block)
		database[block]["id"] = CUSTOM_BLOCK_VANILLA	# Item for placing custom block
		database[block][CATEGORY] = "material"			# Category
		database[block]["custom_data"] = {"smithed":{}}	# Smithed convention
		database[block]["custom_data"]["smithed"]["dict"] = {"block": {material_base: True}}
		if block.endswith("ore"):
			database[block]["custom_data"]["smithed"]["dict"]["ore"] = {material_base: True}
		if block.endswith("block"):
			if block.startswith("raw") and f"raw_{material_base}.png" in TEXTURES_FILES:
				database[block][RESULT_OF_CRAFTING] = [{"type":"crafting_shaped","result_count":1,"group":material_base,"category":"misc","shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr(f"raw_{material_base}")}}]
			else:
				database[block][RESULT_OF_CRAFTING] = [{"type":"crafting_shaped","result_count":1,"group":material_base,"category":"misc","shape":["XXX","XXX","XXX"],"ingredients":{"X":main_ingredient}}]
		pass

	## Ingredients (ingot, nugget, raw, and other)
	for item in [material_base, f"{material_base}_ingot", f"{material_base}_nugget", f"raw_{material_base}", f"{material_base}_fragment", f"{material_base}_dust", f"{material_base}_stick", f"{material_base}_rod"]:
		if item + ".png" not in TEXTURES_FILES:
			continue
		if item not in database:
			database[item] = {}
		warning(item)
		item_type = item.replace(f"{material_base}_", "").replace(f"_{material_base}", "")
		database[item]["id"] = CUSTOM_ITEM_VANILLA		# Custom item
		database[item][CATEGORY] = "material"			# Category
		database[item]["custom_data"] = {"smithed":{}}	# Smithed convention
		database[item]["custom_data"]["smithed"]["dict"] = {item_type: {material_base: True}}

		# Recipes
		database[item][RESULT_OF_CRAFTING] = []
		if item.endswith("ingot") or item.endswith("fragment") or item == material_base:
			if f"{material_base}_block.png" in TEXTURES_FILES:
				database[item][RESULT_OF_CRAFTING].append({"type":"crafting_shapeless","result_count":9,"category":"misc","group":material_base,"ingredients":[ingr_repr(f"{material_base}_block")]})
			if f"{material_base}_nugget.png" in TEXTURES_FILES:
				database[item][RESULT_OF_CRAFTING].append({"type":"crafting_shaped","result_count":1,"category":"misc","group":material_base,"shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr(f"{material_base}_nugget")}})
			if f"raw_{material_base}.png" in TEXTURES_FILES:
				database[item][RESULT_OF_CRAFTING].append({"type":"smelting","result_count":1,"category":"misc","group":material_base,"experience":0.8,"cookingtime":200,"ingredient":ingr_repr(f"raw_{material_base}")})
				database[item][RESULT_OF_CRAFTING].append({"type":"blasting","result_count":1,"category":"misc","group":material_base,"experience":0.8,"cookingtime":100,"ingredient":ingr_repr(f"raw_{material_base}")})
			if f"{material_base}_dust.png" in TEXTURES_FILES:
				database[item][RESULT_OF_CRAFTING].append({"type":"smelting","result_count":1,"category":"misc","group":material_base,"experience":0.8,"cookingtime":200,"ingredient":ingr_repr(f"{material_base}_dust")})
				database[item][RESULT_OF_CRAFTING].append({"type":"blasting","result_count":1,"category":"misc","group":material_base,"experience":0.8,"cookingtime":100,"ingredient":ingr_repr(f"{material_base}_dust")})
			if f"{material_base}_ore.png" in TEXTURES_FILES:
				database[item][RESULT_OF_CRAFTING].append({"type":"smelting","result_count":1,"category":"misc","group":material_base,"experience":0.8,"cookingtime":200,"ingredient":ingr_repr(f"{material_base}_ore")})
				database[item][RESULT_OF_CRAFTING].append({"type":"blasting","result_count":1,"category":"misc","group":material_base,"experience":0.8,"cookingtime":100,"ingredient":ingr_repr(f"{material_base}_ore")})
		if item.endswith("stick"):
			database[item][RESULT_OF_CRAFTING].append({"type":"crafting_shaped","result_count":4,"category":"misc","shape":["X","X"],"ingredients":{"X":main_ingredient}})
		if item.endswith("rod"):
			database[item][RESULT_OF_CRAFTING].append({"type":"crafting_shaped","result_count":1,"category":"misc","shape":["X","X","X"],"ingredients":{"X":main_ingredient}})
		pass

	# Armor (helmet, chestplate, leggings, boots)
	armor_attributes = equipments_config.get_armor_attributes()
	for armor in ["helmet", "chestplate", "leggings", "boots"]:
		armor = material_base + "_" + armor
		if armor + ".png" not in TEXTURES_FILES:
			continue
		if armor not in database:
			database[armor] = {}
		warning(armor)




	error()
	pass

