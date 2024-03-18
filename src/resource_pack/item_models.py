
# Import config
from src.importer import *

# For each item,
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/block", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/item", exist_ok=True)
faces = ["down", "up", "north", "south", "west", "east"]
sides = ["side", "top", "bottom", "front", "back", "inner"]
both = faces + sides
for item, data in DATABASE.items():
	block_or_item = "block" if data["id"] == "minecraft:barrel" else "item"

	# Copy textures to the resource pack
	source = f"{TEXTURES_FOLDER}/{item}.png"
	if os.path.exists(source):
		destination = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/{block_or_item}/{item}.png"
		shutil.copyfile(source, destination)

	# Get all textures for the block
	additional_textures = []
	for root, dirs, files in os.walk(f"{TEXTURES_FOLDER}/"):
		for file in files:
			if file.startswith(item):
				if any(x in file.replace(item, "") for x in both):
					additional_textures.append(file.replace(".png", ""))	# Only keep the textures for sides/faces

				# Copy textures to the resource pack
				source = f"{TEXTURES_FOLDER}/{file}"
				destination = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/{block_or_item}/{file}"
				shutil.copyfile(source, destination)
		pass

	# Generate its model file
	with super_open(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/{block_or_item}/{item}.json", "w") as f:
		if block_or_item == "block":
			"""{
				"parent": "minecraft:block/cube_all",
				"textures": {
					"down": "simplenergy:item/blocks/furnace_generator_top",
					"up": "simplenergy:item/blocks/furnace_generator_top",
					"north": "simplenergy:item/blocks/furnace_generator_front_off",
					"south": "simplenergy:item/blocks/furnace_generator_side",
					"west": "simplenergy:item/blocks/furnace_generator_side",
					"east": "simplenergy:item/blocks/furnace_generator_side"
				},
				"elements": [{
					"from": [ 0, 0, 0 ],
					"to": [ 16, 16, 16 ],
					"faces": {
						"down":  { "texture": "#down", "cullface": "down" },
						"up":    { "texture": "#up", "cullface": "up" },
						"north": { "texture": "#north", "cullface": "north" },
						"south": { "texture": "#south", "cullface": "south" },
						"west":  { "texture": "#west", "cullface": "west" },
						"east":  { "texture": "#east", "cullface": "east" }
					}
				}]
			}"""
			# OR
			content = {"parent": "block/cube_all"}
			content["textures"] = {}

			# If only one, apply everywhere
			if not additional_textures:
				content["textures"]["all"] = f"{NAMESPACE}:{block_or_item}/{item}"
			else:
				# TODO: need to test all cases
				# If more than one, apply to each side
				content["elements"] = [{"from": [0, 0, 0], "to": [16, 16, 16], "faces": {}}]
				for side in faces:

					if f"{item}_{side}" in additional_textures:
						content["textures"][side] = f"{NAMESPACE}:{block_or_item}/{item}_{side}"
						content["elements"][0]["faces"][side] = {"texture": f"#{side}", "cullface": side}
					else:
						content["textures"][side] = f"{NAMESPACE}:{block_or_item}/{item}"
				
				pass

			# TODO: generate placed models for item_display
		
		# Else, it's an item
		else:
			# TODO
			pass
		
		# Write content
		formatted_content = json.dumps(content, indent = '\t')
		f.write(formatted_content + "\n")
	pass
info("Custom models created")

