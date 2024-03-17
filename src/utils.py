
from src.config import *

# Function mainly used for database generation
def ingredient_repr(id: str, count: int|None = None) -> dict:
	""" Get the identity of the ingredient from its id for custom crafts
	Args:
		id	(str): The id of the ingredient, ex: adamantium_ingot
	Returns:
		str: The identity of the ingredient for custom crafts, ex: "custom_data": "imagineyourcraft.adamantium_ingot"
	"""
	if count is None:
		return {"custom_data": f"{NAMESPACE}.{id}"}
	else:
		return {"Count": count, "custom_data": f"{NAMESPACE}.{id}"}

