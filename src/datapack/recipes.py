
# Import config
from config import *
from src.utils.io import *
from src.utils.print import *

# Functions for recipes
def shapeless_recipe(recipe: dict, item: str) -> dict:
	""" Generate the dictionnary for the recipe json file
	Args:
		recipe	(dict):	The recipe to generate
		item	(str):	The item to generate the recipe for
	Returns:
		dict: The generated recipe
	"""
	try:
		data = DATABASE[item]
	except:
		data = EXTERNAL_DATABASE[item]
	to_return = {
		"type": "minecraft:" + recipe["type"],
		"category": recipe[CATEGORY],
		"group": recipe["group"] if recipe.get("group") else None,
		"ingredients": recipe["ingredients"],
		"result": {"id": data["id"], "count": recipe["result_count"]} if not recipe.get("result") else recipe["result"]
	}
	if not to_return["group"]:
		del to_return["group"]
	if not recipe.get("result"):
		for k, v in data.items():
			if k not in NOT_COMPONENTS:
				if to_return["result"].get("components") is None:
					to_return["result"]["components"] = {}
				to_return["result"]["components"][f"minecraft:{k}"] = v
	else:
		# Replace "item" to "id" but keep "id" as the first key 
		result = {"id":to_return["result"]["item"]}
		result.update(to_return["result"])
		result.pop("item")
		to_return["result"] = result
	return to_return

def shaped_recipe(recipe: dict, item: str) -> dict:
	try:
		data = DATABASE[item]
	except:
		data = EXTERNAL_DATABASE[item]
	to_return = {
		"type": "minecraft:" + recipe["type"],
		"category": recipe[CATEGORY],
		"group": recipe["group"] if recipe.get("group") else None,
		"pattern": recipe["shape"],
		"key": recipe["ingredients"],
		"result": {"id": data["id"], "count": recipe["result_count"]} if not recipe.get("result") else recipe["result"]
	}
	if not to_return["group"]:
		del to_return["group"]
	if not recipe.get("result"):
		for k, v in data.items():
			if k not in NOT_COMPONENTS:
				if to_return["result"].get("components") is None:
					to_return["result"]["components"] = {}
				to_return["result"]["components"][f"minecraft:{k}"] = v
	else:
		# Replace "item" to "id" but keep "id" as the first key 
		result = {"id":to_return["result"]["item"]}
		result.update(to_return["result"])
		result.pop("item")
		to_return["result"] = result
	return to_return

# Generate recipes with vanilla input (no components)
generated_recipes = []
for item, data in DATABASE.items():
	crafts = []
	if data.get(RESULT_OF_CRAFTING):
		crafts += data[RESULT_OF_CRAFTING]
	if data.get(USED_FOR_CRAFTING):
		crafts += data[USED_FOR_CRAFTING]
	if crafts:
		i = 1
		for recipe in crafts:

			# Get ingredients
			name = f"{item}" if i == 1 else f"{item}_{i}"
			ingr = recipe.get("ingredients")
			if not ingr:
				ingr = [recipe.get("ingredient")]

			# Shapeless
			if recipe["type"] == "crafting_shapeless":
				if any(i.get("item") == None for i in ingr):
					continue
				r = shapeless_recipe(recipe, item)
				write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/recipes/{name}.json", super_json_dump(r, max_level = 5))
				i += 1
				generated_recipes.append(name)
			elif recipe["type"] == "crafting_shaped":
				if any(i.get("item") == None for i in ingr.values()):
					continue
				r = shaped_recipe(recipe, item)
				write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/recipes/{name}.json", super_json_dump(r, max_level = 5))
				i += 1
				generated_recipes.append(name)
	pass

# Create a function that will give all recipes
content = "\n# Get all recipes\n"
for recipe in generated_recipes:
	content += f"recipe give @s {NAMESPACE}:{recipe}\n"
write_to_file(f"{DATAPACK_FUNCTIONS}/utils/get_all_recipes.mcfunction", content + "\n")
info("Vanilla recipes generated")

