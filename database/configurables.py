
from src.config import *

# Constants
STARTING_CMD = 2015000	# Prefix for custom_model_data
EQUIPMENTS = {
	"helmet":		{"diamond":{"durability":363,"armor":3,"armor_toughness":2},"netherite":{"durability":407,"armor":3,"armor_toughness":3,"knockback_resistance":0.1}},
	"chestplate":	{"diamond":{"durability":528,"armor":8,"armor_toughness":2},"netherite":{"durability":592,"armor":8,"armor_toughness":3,"knockback_resistance":0.1}},
	"leggings":		{"diamond":{"durability":495,"armor":6,"armor_toughness":2},"netherite":{"durability":555,"armor":6,"armor_toughness":3,"knockback_resistance":0.1}},
	"boots":		{"diamond":{"durability":429,"armor":3,"armor_toughness":2},"netherite":{"durability":481,"armor":3,"armor_toughness":3,"knockback_resistance":0.1}},
	"sword":		{"diamond":{"durability":1561,"attack_damage":7,"attack_speed":-2.50},"netherite":{"durability":2031,"attack_damage":8,"attack_speed":-2.50}},
	"pickaxe":		{"diamond":{"durability":1561,"attack_damage":5,"attack_speed":-2.75},"netherite":{"durability":2031,"attack_damage":6,"attack_speed":-2.75}},
	"axe":			{"diamond":{"durability":1561,"attack_damage":9,"attack_speed":-3.00},"netherite":{"durability":2031,"attack_damage":10,"attack_speed":-3.00}},
	"shovel":		{"diamond":{"durability":1561,"attack_damage":5,"attack_speed":-3.00},"netherite":{"durability":2031,"attack_damage":6,"attack_speed":-3.00}},
	"hoe":			{"diamond":{"durability":1561,"attack_damage":1,"attack_speed":0},"netherite":{"durability":2031,"attack_damage":1,"attack_speed":0}},
}

# Constants lists for defining items in link with ores
OTHERS = ["stick", "rod"]
ORES = {
	# All specified data here should be made for a "pickaxe" item
	"adamantium": {"equivalent_to": "netherite", "durability": 1873, "attack_damage":6.2, "speed": 1.2},
	"sapphire": {"equivalent_to": "diamond", "durability": 1752, "attack_damage":5, "speed": 1.2},
	"ruby": {"equivalent_to": "diamond", "durability": 1647, "attack_damage":5.5, "speed": 1.1},
	"topaz": {"equivalent_to": "diamond", "durability": 1281, "attack_damage":6, "speed": 1.0},
	"massive_obsidian": {"equivalent_to": "diamond", "durability": 3902, "attack_damage":4.8, "speed": 0.8},
	"emerald": {"equivalent_to": "diamond", "durability": 736, "attack_damage":5, "speed": 1.0, "luck": 0.25},
	"steel": {"equivalent_to": "diamond", "durability": 444, "attack_damage":4, "speed": 0.7},

	"lignite": {},
	"slate": {},

	"stone": {},
	"old_ruby": {}
}
PLACEABLES = ["block", "ore"]
INGREDIENTS = ["ingot", "nugget", "dust", "fragment", "raw", ""]
ARMORS = list(EQUIPMENTS)[:4]

# Get every item texture paths from textures folder
all_textures = [f for f in os.listdir(TEXTURES_FOLDER) if os.path.isfile(os.path.join(TEXTURES_FOLDER, f))]

# Remove sides and ignored textures
IGNORED_TEXTURES = [f"{ore.replace('massive_','')}_layer_{layer+1}" for ore in ORES for layer in range(2)]
IGNORED_TEXTURES += ["red_light_on"]
IGNORED_TEXTURES = [t + ".png" for t in IGNORED_TEXTURES]	# Add .png to the list
textures_filenames = [f for f in all_textures if not any(s in f for s in SIDES) and f not in IGNORED_TEXTURES]

