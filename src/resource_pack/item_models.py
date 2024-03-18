
# Import config
from src.importer import *

# Make directories
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/block", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/item", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/block", exist_ok=True)
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/item", exist_ok=True)

# Get every block variant
faces = ["down", "up", "north", "south", "west", "east"]
sides = ["bottom", "top", "front", "back", "left", "right", "side"]
both = faces + sides
armors = ["helmet", "chestplate", "leggings", "boots"]

def custom_separators(level):
    if level <= 2:
        return (",", ": ")
    else:
        return (",", " ")

# For each item,
# TODO "_on"
for item, data in DATABASE.items():
	block_or_item = "block" if data["id"] == "minecraft:barrel" else "item"
	dest_base_model = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/{block_or_item}"
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
					additional_textures.append(file.replace(".png", ""))	# Only keep the textures for sides/faces

				# Copy textures to the resource pack
				source = f"{TEXTURES_FOLDER}/{file}"
				destination = f"{dest_base_textu}/{file}"
				shutil.copyfile(source, destination)
		pass

	# Generate its model file
	with super_open(f"{dest_base_model}/{item}.json", "w") as f:
		if block_or_item == "block":
			content = {"parent": "block/cube_all"}
			content["textures"] = {}

			# If only one, apply everywhere
			if not additional_textures:
				content["textures"]["all"] = f"{NAMESPACE}:{block_or_item}/{item}"

			# If more than one, apply to each side
			else:
				content["elements"] = [{"from": [0, 0, 0], "to": [16, 16, 16], "faces": {}}]

				# Generate links between faces and textures
				for face in faces:
					content["elements"][0]["faces"][face] = {"texture": f"#{face}", "cullface": face}
	
				# For each possible side (in reverse order)
				for i in range(len(sides), 0, -1):
					side = sides[i - 1]
    
					# If we have a texture for the side
					if any(side in x for x in additional_textures):
						path = f"{NAMESPACE}:{block_or_item}/{item}_{side}"
						
						# If it's a side, apply to all faces (as it is first, it will be overwritten by the others)
						if side == "side":
							for face in faces:
								content["textures"][face] = path
						# Else, apply the texture to the face with the same name
						else:
							face = faces[i - 1]
							content["textures"][face] = path
    
							# Exception: apply top texture also to bottom
							if face == "up":
								content["textures"]["down"] = path
				pass

			# TODO: generate placed models for item_display
		
		# Else, it's an item
		else:
			# If not an armor
			path = f"{NAMESPACE}:{block_or_item}/{item}"
			if not any(x in item for x in armors):
				content = {"parent": "item/handheld", "textures": {"layer0": path}}
			else:
				content = {"parent": "item/generated", "textures": {"layer0": path}}
				content["textures"]["layer1"] = content["textures"]["layer0"]
			pass
		
		# Write content
		formatted_content = json.dumps(content, indent = '\t')
		f.write(formatted_content + "\n")
	pass
info("Custom models created")

