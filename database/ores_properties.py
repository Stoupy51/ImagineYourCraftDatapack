
# Imports
from src.importer import *
from database.configurables import *

# For each ore, apply new properties
SLOTS = {"helmet": "head", "chestplate": "chest", "leggings": "legs", "boots": "feet", "sword": "mainhand", "pickaxe": "mainhand", "axe": "mainhand", "shovel": "mainhand", "hoe": "mainhand"}
for ore, data in ORES.items():
	if data == {}:
		continue
	id = ore.replace("massive_","")

	# Get the durability, attack_damage, and speed multipliers
	durability = data["durability"] / EQUIPMENTS["pickaxe"][data["equivalent_to"]]["durability"]
	damage_resist = data["attack_damage"] / EQUIPMENTS["pickaxe"][data["equivalent_to"]]["attack_damage"]
	speed = data["speed"] - 1

	# For each available equipment,
	for e in EQUIPMENTS:
		item = f"{id}_{e}"
		if item not in DATABASE:
			continue

		# Get new properties and updated them
		equivalent = EQUIPMENTS[e][data["equivalent_to"]].copy()
		equivalent["durability"] = int(equivalent["durability"] * durability)
		if "armor" in equivalent:
			equivalent["armor"] = round(equivalent["armor"] * damage_resist, 1)
		if "attack_damage" in data and "attack_damage" in equivalent:
			equivalent["attack_damage"] = round(equivalent["attack_damage"] * damage_resist, 1)
		if "luck" in data:
			equivalent["luck"] = data["luck"]

		# Update the item components
		DATABASE[item]["attribute_modifiers"]= []
		if "attack_damage" in equivalent:
			uuid = UUIDS["attack_damage"][e]
			name = "generic.attack_damage"
			DATABASE[item]["attribute_modifiers"].append({"type":name,"uuid":uuid,"name":name,"amount":equivalent["attack_damage"],"operation":"add_value","slot":"mainhand"})
			offset = 0
			attack_speed = EQUIPMENTS[e][data["equivalent_to"]]["attack_speed"] - offset
			uuid = UUIDS["attack_speed"][e]
			DATABASE[item]["attribute_modifiers"].append({"type":"generic.attack_speed","uuid":uuid,"name":"generic.attack_speed","amount":attack_speed,"operation":"add_value","slot":"mainhand"})
		
		if "armor" in equivalent:
			uuid = UUIDS["armor"][e]
			name = "generic.armor"
			DATABASE[item]["attribute_modifiers"].append({"type":name,"uuid":uuid,"name":name,"amount":equivalent["armor"],"operation":"add_value","slot":SLOTS[e]})
		
		if "armor_toughness" in equivalent:
			uuid = UUIDS["armor_toughness"][e]
			name = "generic.armor_toughness"
			DATABASE[item]["attribute_modifiers"].append({"type":name,"uuid":uuid,"name":name,"amount":equivalent["armor_toughness"],"operation":"add_value","slot":SLOTS[e]})
		
		if "knockback_resistance" in equivalent:
			uuid = UUIDS["knockback_resistance"][e]
			name = "generic.knockback_resistance"
			DATABASE[item]["attribute_modifiers"].append({"type":name,"uuid":uuid,"name":name,"amount":equivalent["knockback_resistance"],"operation":"add_value","slot":SLOTS[e]})
		
		if "luck" in equivalent:
			uuid = UUIDS["luck"][e]
			name = "generic.luck"
			DATABASE[item]["attribute_modifiers"].append({"type":name,"uuid":uuid,"name":name,"amount":equivalent["luck"],"operation":"add_value","slot":SLOTS[e]})
		
		if "durability" in equivalent:
			DATABASE[item]["max_damage"] = equivalent["durability"]
		
		if "speed" in data and "attack_speed" in equivalent:
			uuid = UUIDS["mining_speed"][e]
			DATABASE[item]["attribute_modifiers"].append({"type":"player.block_break_speed","uuid":uuid,"name":"player.block_break_speed","amount":speed,"operation":"add_value","slot":"mainhand"})
info("Added new properties to each ore item")

