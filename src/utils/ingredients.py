
from src.config import NAMESPACE

# Function mainly used for database generation
def ingr_repr(id: str, count: int|None = None) -> dict:
	""" Get the identity of the ingredient from its id for custom crafts
	Args:
		id	(str): The id of the ingredient, ex: adamantium_ingot
	Returns:
		str: The identity of the ingredient for custom crafts,
			ex: {"components":{"custom_data":{imagineyourcraft:{adamantium_ingot=True}}}}
			ex: {"item": "minecraft:stick"}
	"""
	if ":" in id:
		to_return = {"item": id}
	else:
		to_return = {"components":{"custom_data":{NAMESPACE:{id:True}}}}
	if count is not None:
		to_return["count"] = count
	return to_return

# Mainly used for manual
def ingr_to_id(ingredient: dict, add_namespace: bool = True) -> str:
	""" Get the id from an ingredient dict
	Args:
		ingredient (dict): The ingredient dict
			ex: {"components":{"custom_data":{imagineyourcraft:{adamantium_ingot=True}}}}
			ex: {"item": "minecraft:stick"}
	Returns:
		str: The id of the ingredient, ex: "minecraft:stick" or "imagineyourcraft:adamantium_ingot"
	"""
	if ingredient.get("item"):
		if not add_namespace:
			return ingredient["item"].split(":")[1]
		return ingredient["item"]
	else:
		custom_data = ingredient["components"]["custom_data"]
		namespace = list(custom_data.keys())[0]
		id = list(custom_data[namespace].keys())[0]
		if add_namespace:
			return namespace + ":" + id
		return id

