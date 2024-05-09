
## TODO: verify database and dump it before hand
from config import *
from src.utils.ingredients import *
from src.utils.print import *
from src.utils.io import *

# Export database to JSON for debugging generation
with super_open(DATABASE_DEBUG, "w") as f:
	super_json_dump(DATABASE, f)
debug(f"Received database exported to '{DATABASE_DEBUG}'")

# Check every single thing in the database
errors = []
for item, data in DATABASE.items():

	# Check for a proper ID
	if not data.get("id"):
		errors.append(f"'id' key missing for '{item}'")
	else:
		if not isinstance(data["id"], str):
			errors.append(f"'id' key should be a string for '{item}'")
		elif data["id"] == "minecraft:deepslate":
			errors.append(f"'id' key should not be 'minecraft:deepslate' for '{item}', it's a reserved ID")
		
		# Force VANILLA_BLOCK key for custom blocks
		elif data["id"] in [CUSTOM_BLOCK_VANILLA, CUSTOM_BLOCK_ALTERNATIVE] and not data.get(VANILLA_BLOCK):
			errors.append(f"VANILLA_BLOCK key missing for '{item}', needed format: VANILLA_BLOCK: \"minecraft:stone\"")

		# Prevent the use of "container" key for custom blocks
		elif data["id"] == CUSTOM_BLOCK_VANILLA and data.get("container"):
			errors.append(f"'container' key should not be used for '{item}', it's a reserved key for custom blocks, prefer using COMMANDS_ON_PLACEMENT key to fill in the container")

	# If a category is present but wrong format, log an error
	if data.get(CATEGORY) and not isinstance(data[CATEGORY], str):
		errors.append(f"CATEGORY key should be a string for '{item}'")

	# Check for a proper custom data
	if data.get("custom_data") and not isinstance(data["custom_data"], dict):
		errors.append(f"'custom_data' key should be a dictionary for '{item}'")
	elif not data.get("custom_data") or not data["custom_data"].get(NAMESPACE) or not isinstance(data["custom_data"][NAMESPACE], dict) or not data["custom_data"][NAMESPACE].get(item) or not isinstance(data["custom_data"][NAMESPACE][item], bool):
		errors.append(f"'custom_data' key missing proper data for '{item}', should have at least \"custom_data\": {{NAMESPACE: {{\"{item}\": True}}}}")

	# Check for wrong custom ores data
	if data.get(VANILLA_BLOCK) == VANILLA_BLOCK_FOR_ORES and not data.get(NO_SILK_TOUCH_DROP):
		errors.append(f"NO_SILK_TOUCH_DROP key missing for '{item}', should be the ID of the block that drops when mined without silk touch")
	if data.get(VANILLA_BLOCK) != VANILLA_BLOCK_FOR_ORES and data.get(NO_SILK_TOUCH_DROP):
		errors.append(f"NO_SILK_TOUCH_DROP key should not be used for '{item}' if it doesn't use VANILLA_BLOCK_FOR_ORES")
	if data.get(NO_SILK_TOUCH_DROP) and not isinstance(data[NO_SILK_TOUCH_DROP], str):
		errors.append(f"NO_SILK_TOUCH_DROP key should be a string for '{item}', ex: \"adamantium_fragment\" or \"minecraft:stone\"")

	# Force the use of "item_name" key for every item
	if not data.get("item_name") or not isinstance(data["item_name"], str):
		errors.append(f"'item_name' key missing or not a string for '{item}'")
	
	# Warn if no custom model data
	if not data.get("custom_model_data"):
		warning(f"'custom_model_data' key missing for '{item}', ignore if it's on purpose")
	
	# Check all the recipes
	if data.get(RESULT_OF_CRAFTING) or data.get(USED_FOR_CRAFTING):

		# Get a list of recipes
		crafts_to_check = data.get(RESULT_OF_CRAFTING)
		crafts_to_check = [] if not crafts_to_check else crafts_to_check
		if data.get(USED_FOR_CRAFTING):
			crafts_to_check += data[USED_FOR_CRAFTING]

		# Check each recipe
		if not isinstance(crafts_to_check, list):
			errors.append(f"RESULT_OF_CRAFTING key should be a list of recipes for '{item}'")
		else:
			for i, recipe in enumerate(crafts_to_check):

				# A recipe is always a dictionnary
				if not isinstance(recipe, dict):
					errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should be a dictionary for '{item}'")
				else:

					# Verify "type" key
					if not recipe.get("type") or not isinstance(recipe["type"], str):
						errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a string 'type' key for '{item}'")
					else:

						# Check the crafting_shaped type
						if recipe["type"] == "crafting_shaped":
							if not recipe.get("shape") or not isinstance(recipe["shape"], list):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a list[str] 'shape' key for '{item}'")
							elif len(recipe["shape"]) > 3 or len(recipe["shape"][0]) > 3:
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a maximum of 3 rows and 3 columns for '{item}'")
							else:
								row_size = len(recipe["shape"][0])
								if any(len(row) != row_size for row in recipe["shape"]):
									errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have the same number of columns for each row for '{item}'")
								
							if not recipe.get("ingredients") or not isinstance(recipe["ingredients"], dict):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict 'ingredients' key for '{item}'")
							else:
								for symbol, ingredient in recipe["ingredients"].items():
									if not isinstance(ingredient, dict):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict ingredient for symbol '{symbol}' for '{item}'")
									elif not ingredient.get("item") and not ingredient.get("components"):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have an 'item' or 'components' key for ingredient of symbol '{symbol}' for '{item}', please use 'ingr_repr' function")
									elif ingredient.get("components") and not isinstance(ingredient["components"], dict):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict 'components' key for ingredient of symbol '{symbol}' for '{item}', please use 'ingr_repr' function")
									if not any(symbol in line for line in recipe["shape"]):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a symbol '{symbol}' in the shape for '{item}'")

						# Check the crafting_shapeless type
						elif recipe["type"] == "crafting_shapeless":
							if not recipe.get("ingredients") or not isinstance(recipe["ingredients"], list):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a list 'ingredients' key for '{item}'")
							else:
								for ingredient in recipe["ingredients"]:
									if not isinstance(ingredient, dict):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict ingredient for '{item}'")
									elif not ingredient.get("item") and not ingredient.get("components"):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have an 'item' or 'components' key for ingredient for '{item}', please use 'ingr_repr' function")
									elif ingredient.get("components") and not isinstance(ingredient["components"], dict):
										errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict 'components' key for ingredient for '{item}', please use 'ingr_repr' function")
						
						# Check the furnaces recipes
						elif recipe["type"] in FURNACES_RECIPES_TYPES:
							if not recipe.get("ingredient") or not isinstance(recipe["ingredient"], dict):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict 'ingredient' key for '{item}'")
							elif not recipe["ingredient"].get("item") and not recipe["ingredient"].get("components"):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have an 'item' or 'components' key for ingredient for '{item}', please use 'ingr_repr' function")
							elif recipe["ingredient"].get("components") and not isinstance(recipe["ingredient"]["components"], dict):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a dict 'components' key for ingredient for '{item}', please use 'ingr_repr' function")
							
							if not recipe.get("experience") or not isinstance(recipe["experience"], (float, int)):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have a float 'experience' key for '{item}'")
							if not recipe.get("cookingtime") or not isinstance(recipe["cookingtime"], int):
								errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have an int 'cookingtime' key for '{item}'")

					# Check the result count
					if not recipe.get("result_count") or not isinstance(recipe["result_count"], int):
						errors.append(f"Recipe #{i} in RESULT_OF_CRAFTING should have an int 'result_count' key for '{item}'")

	# Commands on custom block placement
	if data.get(COMMANDS_ON_PLACEMENT) and data.get("id"):
		if data["id"] not in [CUSTOM_BLOCK_VANILLA, CUSTOM_BLOCK_ALTERNATIVE]:
			errors.append(f"COMMANDS_ON_PLACEMENT key should only be used for custom blocks for '{item}'")
		elif not isinstance(data[COMMANDS_ON_PLACEMENT], (list, str)):
			errors.append(f"COMMANDS_ON_PLACEMENT key should be a list of string or a string for '{item}'")
		elif isinstance(data[COMMANDS_ON_PLACEMENT], list):
			for i, command in enumerate(data[COMMANDS_ON_PLACEMENT]):
				if not isinstance(command, str):
					errors.append(f"Command #{i} in COMMANDS_ON_PLACEMENT should be a string for '{item}'")
	
	# Commands on custom block break
	if data.get(COMMANDS_ON_BREAK) and data.get("id"):
		if data["id"] not in [CUSTOM_BLOCK_VANILLA, CUSTOM_BLOCK_ALTERNATIVE]:
			errors.append(f"COMMANDS_ON_BREAK key should only be used for custom blocks for '{item}'")
		elif not isinstance(data[COMMANDS_ON_BREAK], (list, str)):
			errors.append(f"COMMANDS_ON_BREAK key should be a list of string or a string for '{item}'")
		elif isinstance(data[COMMANDS_ON_BREAK], list):
			for i, command in enumerate(data[COMMANDS_ON_BREAK]):
				if not isinstance(command, str):
					errors.append(f"Command #{i} in COMMANDS_ON_BREAK should be a string for '{item}'")


# Log errors if any
if errors:
	error("Errors found in the database during verification:\n" + "\n".join(errors))
else:
	info("No errors found in the database during verification")


# Add additional data to the custom blocks
for item, data in DATABASE.items():
	if data["id"] == CUSTOM_BLOCK_VANILLA:
		data["container"] = [{"slot": 0, "item": {"id": "minecraft:stone", "count": 1,"components": {"minecraft:custom_data": {"smithed": {"block": {"id": f"{NAMESPACE}:{item}", "from": NAMESPACE}}}}}}]

