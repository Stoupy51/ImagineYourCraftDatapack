
from src.config import *

# Function mainly used for database generation
def ingredient_repr(id: str, count: int|None = None) -> str:
	""" Get the identity of the ingredient from its id
	Args:
		id	(str): The id of the ingredient, ex: adamantium_ingot
	Returns:
		str: The identity of the ingredient for custom crafts, ex: "custom_data": "imagineyourcraft.adamantium_ingot"
	"""
	if count is None:
		return f'"custom_data": "{NAMESPACE}.{id}"'
	else:
		return f'{{"Count":{count}, "custom_data": "{NAMESPACE}.{id}"}}'

