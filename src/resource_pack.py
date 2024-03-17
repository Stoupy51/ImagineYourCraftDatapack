
# Import config
from src.importer import *
print()

# Get every vanilla IDs
vanilla_ids = []
for v in DATABASE.values():
	if v["id"] not in vanilla_ids:
		vanilla_ids.append(v["id"].replace("minecraft:", ""))

# For each vanilla ID, create the json model file
blocks = ["barrel", "command_block"]
for id in vanilla_ids:
	with super_open(f"{BUILD_RESOURCE_PACK}/assets/minecraft/models/item/{id}.json", "w") as file:
		block_or_item = "block" if id in blocks else "item"
		content = {"parent": f"{block_or_item}/{id}", "overrides": "__LIST__"}
		formatted_content = json.dumps(content, indent = '\t')

		# Get overrides
		overrides = []
		for item, data in DATABASE.items():
			if data["id"].replace("minecraft:","") == id:
				overrides.append(f'{{"predicate": {{ "custom_model_data": {data["custom_model_data"]}}}, "model": "{NAMESPACE}:{block_or_item}/{item}" }}')
		overrides = ",\n\t\t".join(overrides)

		# Write the content to the file
		file.write(formatted_content.replace('"__LIST__"', f'[\n\t\t{overrides}\n\t]') + "\n")
	pass
info("Vanilla models created")

# For each item,
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/block", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/item", exist_ok=True)
faces = ["down", "up", "north", "south", "west", "east"]
sides = ["side", "top", "bottom", "front", "back"]
for item, data in DATABASE.items():
	block_or_item = "block" if data["id"] == "minecraft:barrel" else "item"

	# Copy textures to the resource pack
	source = f"{TEXTURES_FOLDER}/{item}.png"
	destination = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/{block_or_item}/{item}.png"
	shutil.copyfile(source, destination)

	# Get all textures for the block
	textures_path_list = []
	for root, dirs, files in os.walk(f"{TEXTURES_FOLDER}/"):
		for file in files:
			if file.startswith(item):
				textures_path_list.append(file.replace(".png", ""))

				# Copy textures to the resource pack
				source = f"{TEXTURES_FOLDER}/{file}"
				destination = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/{block_or_item}/{file}"
				shutil.copyfile(source, destination)
		pass
	textures_path_list = [path for path in textures_path_list if path != item and any(face in path for face in faces)]	# Only keep the textures for sides/faces

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
			if not textures_path_list:
				content["textures"]["all"] = f"{NAMESPACE}:{block_or_item}/{item}"
			else:
				# TODO: need to test all cases
				# If more than one, apply to each side
				content["elements"] = [{"from": [0, 0, 0], "to": [16, 16, 16], "faces": {}}]
				for side in faces:

					if f"{item}_{side}" in textures_path_list:
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

