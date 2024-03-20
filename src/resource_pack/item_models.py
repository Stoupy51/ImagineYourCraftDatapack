
# Import config
from src.importer import *

# Make directories
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/block/for_item_display", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/item", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/block", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/item", exist_ok=True)

# Get every block variant
both = FACES + SIDES
armors = ["helmet", "chestplate", "leggings", "boots"]
tools = ["sword", "pickaxe", "axe", "shovel", "hoe"]

# For each item,
for item, data in DATABASE.items():
	block_or_item = "block" if data["id"] == "minecraft:barrel" else "item"
	dest_base_textu = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/{block_or_item}"

	# Copy textures to the resource pack
	source = f"{TEXTURES_FOLDER}/{item}.png"
	if os.path.exists(source):
		destination = f"{dest_base_textu}/{item}.png"
		shutil.copyfile(source, destination)

	# Get all textures for the block
	additional_textures = []
	for root, dirs, files in os.walk(f"{TEXTURES_FOLDER}/"):
		for file in files:
			if file.startswith(item):
				if any(x in file.replace(item, "") for x in both):
					additional_textures.append(file.replace(".png", ""))	# Only keep the textures for SIDES/FACES

				# Copy textures to the resource pack
				source = f"{TEXTURES_FOLDER}/{file}"
				destination = f"{dest_base_textu}/{file}"
				shutil.copyfile(source, destination)
		pass

	# Generate its model file
	powered = ["","_on"] if any(x for x in additional_textures if x.endswith("_on")) > 0 else [""]
	for on_off in powered:
		dest_base_model = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/{block_or_item}"
		with super_open(f"{dest_base_model}/{item}{on_off}.json", "w") as f:
			if block_or_item == "block":
				content = {"parent": "block/cube_all"}
				content["textures"] = {}

				# If only one, apply everywhere
				if not additional_textures:
					content["textures"]["all"] = f"{NAMESPACE}:{block_or_item}/{item}"

				# If more than one, apply to each side
				else:
					content["elements"] = [{"from": [0, 0, 0], "to": [16, 16, 16], "faces": {}}]

					# Generate links between FACES and textures
					for face in FACES:
						content["elements"][0]["faces"][face] = {"texture": f"#{face}", "cullface": face}
		
					# For each possible side (in reverse order)
					for i in range(len(SIDES), 0, -1):
						side = SIDES[i - 1]
		
						# If we have a texture for the side
						if any(side in x for x in additional_textures):

							# Get path
							path = f"{NAMESPACE}:{block_or_item}/{item}_{side}"
							if on_off == "_on" and f"{item}_{side}_on" in additional_textures:
								path += "_on"

							# If it's a side, apply to all FACES (as it is first, it will be overwritten by the others)
							if side == "side":
								for face in FACES:
									content["textures"][face] = path

							# Else, apply the texture to the face with the same name
							else:
								face = FACES[i - 1]
								content["textures"][face] = path
		
								# Exception: apply top texture also to bottom
								if face == "up":
									content["textures"]["down"] = path
					pass

			# Else, it's an item
			else:

				path = f"{NAMESPACE}:{block_or_item}/{item}{on_off}"
				content = {"parent": "item/generated",	"textures": {"layer0": path}}
				if any(x in item for x in armors):
					content["textures"]["layer1"] = content["textures"]["layer0"]
				if any(x in item for x in tools):
					content["parent"] = "item/handheld"
				pass
			
			# Write content
			super_json_dump(content, f, max_level = 4)

		# Generate placed models for item_display if it's a block
		if block_or_item == "block":
			dest_base_model = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/{block_or_item}/for_item_display"
			content["display"] = MODEL_DISPLAY
			with super_open(f"{dest_base_model}/{item}{on_off}.json", "w") as f:
				super_json_dump(content, f, max_level = 4)
	pass
info("Custom models created")

