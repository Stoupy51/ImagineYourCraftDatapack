
# Imports
from python_datapack.utils.database_helper import *

# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def main(config: dict) -> None:
    database: dict[str, dict] = config["database"]
    namespace: str = config["namespace"]

    # Write to tick
    write_to_tick_file(config, f"""
# Check for bolts
execute as @e[type=arrow,tag=!{namespace}.bolt_checked] run function {namespace}:entity/bolt_check

# Check for rocks
execute if score #rock_markers {namespace}.data matches 1.. as @e[tag={namespace}.rock_marker,predicate=!{namespace}:has_vehicle] at @s positioned ~ ~-0.5 ~ run function {namespace}:entity/rock_check/marker_final
execute as @e[type=snowball,tag=!{namespace}.rock_checked] run function {namespace}:entity/rock_check/main
""")

	# Prepare ore configs
    ore_configs: dict[str, list[CustomOreGeneration]] = {}
    for base_material, per_region in [("adamantium", 1), ("sapphire", 1), ("ruby", 1), ("topaz", 1), ("steel", 2)]:

        # Add overworld ore
        ore_configs[f"{base_material}_ore"] = [
            CustomOreGeneration(
                dimensions = ["minecraft:overworld"],
                maximum_height = 50,
                minimum_height = 0,
                veins_per_region = per_region,
                vein_size_logic = 0.4,
            )
        ]

        # Add deepslate ore if it exists
        if f"deepslate_{base_material}_ore" in database:
            ore_configs[f"deepslate_{base_material}_ore"] = [
                CustomOreGeneration(
                    dimensions = ["minecraft:overworld"],
                    maximum_height = 0,
                    veins_per_region = per_region,
                    vein_size_logic = 0.4,
                )
            ]

    # Generate ores in the world
    CustomOreGeneration.all_with_config(config, ore_configs)


    pass

