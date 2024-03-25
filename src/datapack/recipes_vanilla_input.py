
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
generated_recipes = []
for item, data in DATABASE.items():
	if data.get(RESULT_OF_CRAFTING) and data[RESULT_OF_CRAFTING] != []:
		i = 1
		for recipe in data[RESULT_OF_CRAFTING]:

			# Get ingredients
			name = f"{item}" if i == 1 else f"{item}_{i}"
			ingr = recipe.get("ingredients")
			if not ingr:
				ingr = [recipe.get("ingredient")]

			# Shapeless
			if recipe["type"] == "crafting_shapeless":
				if any(i.get("item") == None for i in ingr):
					continue
				r = RecipeShapeless(recipe, item)
				with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/recipes/{name}.json", "w") as f:
					super_json_dump(r, f, max_level = -1)
					i += 1
				generated_recipes.append(name)
			elif recipe["type"] == "crafting_shaped":
				if any(i.get("item") == None for i in ingr.values()):
					continue
				r = RecipeShaped(recipe, item)
				with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/recipes/{name}.json", "w") as f:
					super_json_dump(r, f, max_level = -1)
					i += 1
				generated_recipes.append(name)
	pass

# Create a function that will give all recipes
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/utils/get_all_recipes.mcfunction", "w") as f:
	content = "\n# Get all recipes\n"
	for recipe in generated_recipes:
		content += f"recipe give @s {NAMESPACE}:{recipe}\n"
	f.write(content + "\n")
info("Vanilla recipes generated")

