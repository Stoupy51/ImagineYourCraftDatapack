
# Import config
from src.importer import *

# Functions for recipes
def RecipeShapeless(recipe: dict, item: str) -> dict:
	""" Generate the dictionnary for the recipe json file
	Args:
		recipe	(dict):	The recipe to generate
		item	(str):	The item to generate the recipe for
	Returns:
		dict: The generated recipe
	"""
	data = DATABASE[item]
	to_return = {
		"type": "minecraft:" + recipe["type"],
		"category": recipe["category"],
		"ingredients": recipe["ingredients"],
		"result": {"id": data["id"], "count": recipe["result_count"]}
	}
	if recipe.get("group"):
		to_return["group"] = recipe["group"]
	for k, v in data.items():
		if k not in NOT_COMPONENTS:
			if to_return["result"].get("components") is None:
				to_return["result"]["components"] = {}
			to_return["result"]["components"][f"minecraft:{k}"] = v
	return to_return

def RecipeShaped(recipe: dict, item: str) -> dict:
	data = DATABASE[item]
	to_return = {
		"type": "minecraft:" + recipe["type"],
		"category": recipe["category"],
		"pattern": recipe["shape"],
		"key": recipe["ingredients"],
		"result": {"id": data["id"], "count": recipe["result_count"]}
	}
	if recipe.get("group"):
		to_return["group"] = recipe["group"]
	for k, v in data.items():
		if k not in NOT_COMPONENTS:
			if to_return["result"].get("components") is None:
				to_return["result"]["components"] = {}
			to_return["result"]["components"][f"minecraft:{k}"] = v
	return to_return

# Generate recipes with vanilla input (no components)
for item, data in DATABASE.items():
	if data.get(CRAFTING_RECIPES) and data[CRAFTING_RECIPES] != []:
		i = 1
		for recipe in data[CRAFTING_RECIPES]:

			# Get ingredients
			ingr = recipe.get("ingredients")
			if not ingr:
				ingr = [recipe.get("ingredient")]

			# Shapeless
			if recipe["type"] == "crafting_shapeless":
				if any(i.get("item") == None for i in ingr):
					continue
				r = RecipeShapeless(recipe, item)
				with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/recipes/{item}_{i}.json", "w") as f:
					super_json_dump(r, f, max_level = -1)
					i += 1
			elif recipe["type"] == "crafting_shaped":
				if any(i.get("item") == None for i in ingr.values()):
					continue
				r = RecipeShaped(recipe, item)
				with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/recipes/{item}_{i}.json", "w") as f:
					super_json_dump(r, f, max_level = -1)
					i += 1

