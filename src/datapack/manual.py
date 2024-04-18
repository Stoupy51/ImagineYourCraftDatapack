
# Import config
from src.importer import *

## TODO : Add a category for each item

# Generate categories list
categories = {}
for item, data in DATABASE.items():
	if "category" not in data:
		warning(f"Item '{item}' has no category key. Skipping.")
		continue

	category = data["category"]
	if category not in categories:
		categories[category] = []
	categories[category].append(item)

# Debug categories and sizes
s = ""
for category, items in categories.items():
	s += f"\n{category}: {len(items)} items"
info(f"Found {len(categories)} categories:{s}")

