
# Import config
from src.importer import *

## Finally, for each .mcfunction file, add small header (called by what functions)
# Get all mcfunctions paths
mcfunctions = {}
functions_folder = f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/"
for root, _, files in os.walk(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/"):
	for file in files:
		if file.endswith(".mcfunction"):
			to_be_called = f"{NAMESPACE}:" + f"{root}/{file}".replace(functions_folder, "").replace(".mcfunction","")
			mcfunctions[to_be_called] = {"path":f"{root}/{file}", "within":[]}
	pass

"""
#> simplenergy:tick
#
# @within			simplenergy:utils/tick_verification
#"""
# For each json file, get the functions that it calls
functions_tags_folder = f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/"
for root, _, files in os.walk(functions_tags_folder):
	for file in files:
		if file.endswith(".json"):
			to_be_called = f"#{NAMESPACE}:" + f"{root}/{file}".replace(functions_tags_folder, "").replace(".json","")
			with super_open(f"{root}/{file}", "r") as f:
				data = json.load(f)
				if data.get("values"):
					for value in data["values"]:
						calling = value if type(value) == str else value["id"]
						if calling in mcfunctions.keys():
							mcfunctions[calling]["within"].append(to_be_called)
	pass

# For each mcfunction file, get the function that it calls
for file, data in mcfunctions.items():
	with super_open(data["path"], "r") as f:
		for line in f.readlines():
			if "function " in line:
				splitted = line.split("function ")[1].replace("\n","").split(" ")
				calling = splitted[0]
				more = ""
				if len(splitted) > 0:
					more = " " + " ".join(splitted[1:]) # Add Macros or schedule time
				if calling in mcfunctions.keys():
					mcfunctions[calling]["within"].append(file + more)
	pass

# For each mcfunction file, add the header
for file, data in mcfunctions.items():
	if data["within"]:
		withins = "\n#\t\t\t".join(w.strip() for w in data["within"])
		with super_open(data["path"], "r") as f:
			content = "".join(f.readlines())
		with super_open(data["path"], "w") as f:
			header = f"""
#> {file} (Autogenerated)
#
# @within\t{withins}
#"""
			f.write(header + content)
	pass
info("Headers added to all mcfunction files")

