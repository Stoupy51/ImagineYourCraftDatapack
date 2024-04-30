
## TODO: verify database and dump it before hand
from config import *

# Add additional data to the custom blocks
for item, data in DATABASE.items():
	if data["id"] == CUSTOM_BLOCK_VANILLA:
		data["container"] = [{"slot": 0, "item": {"id": "minecraft:stone", "count": 1,"components": {"minecraft:custom_data": {"smithed": {"block": {"id": f"{NAMESPACE}:{item}", "from": NAMESPACE}}}}}}]

