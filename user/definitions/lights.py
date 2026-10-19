""" Light blocks of the mod: log and iron lanterns, the red light, the always lit lamp, the transparent light block, colored lamps and rods, the lignite torch. """
# Imports
from stewbeet import CraftingShapedRecipe, Ingr

from user.definitions.common import COLORS, dyed
from user.original.blocks import Interaction, OriginalBlock, Schema

# Constants
LANTERN_WOODS: list[str] = ["oak", "spruce", "birch", "jungle"]
""" Log lanterns (`gu_1`), 8 logs around glowstone. """

LIGHT_HOST: str = "minecraft:ochre_froglight"
""" A full block giving light 15 and dropping itself. """


# Functions
def main() -> None:
	for wood in LANTERN_WOODS:
		OriginalBlock(
			id=f"{wood}_wood_lantern", host=LIGHT_HOST, variants=((f"{wood}_lantern", ""),), schema=Schema.FIXED, inventory_model=f"lantern_{wood}",
		).define(recipes=[CraftingShapedRecipe(
			result_count=4, category="building", group="wood_lantern", shape=["###", "#X#", "###"],
			ingredients={"#": Ingr(f"minecraft:{wood}_log"), "X": Ingr("minecraft:glowstone")},
		)])
	OriginalBlock(
		id="iron_lantern", host=LIGHT_HOST, variants=(("iron_lantern", ""),), schema=Schema.FIXED, inventory_model="lantern_iron",
	).define(recipes=[CraftingShapedRecipe(
		result_count=4, category="building", shape=["###", "#X#", "###"],
		ingredients={"#": Ingr("minecraft:iron_ingot"), "X": Ingr("minecraft:glowstone")},
	)])
	OriginalBlock(
		id="red_light", host="minecraft:redstone_lamp", variants=(("red_light_off", "lit=false"), ("red_light_on", "lit=true")),
		schema=Schema.LAMP, inventory_model="red_light_off",
	).define(manual_category="redstone", recipes=[CraftingShapedRecipe(
		category="redstone", shape=["###", "#O#", "###"], ingredients={"#": Ingr("minecraft:redstone"), "O": Ingr("minecraft:redstone_lamp")},
	)])
	OriginalBlock(
		id="redstone_lamp_always", host=LIGHT_HOST, variants=(("redstone_lamp_always", ""),), schema=Schema.FIXED,
		inventory_model="legacy/lit_redstone_lamp",
	).define(manual_category="redstone")
	OriginalBlock(
		id="transparent_light_block", host="minecraft:light[level=15]", variants=(("transparent_light_block", ""),), schema=Schema.FIXED,
		interaction=Interaction(),
	).define(recipes=[CraftingShapedRecipe(
		result_count=4, category="building", shape=["###", "#X#", "###"], ingredients={"#": Ingr("minecraft:glass"), "X": Ingr("minecraft:glowstone")},
	)])
	OriginalBlock(id="lignite_torch", host="minecraft:torch", variants=(("lignite_torch", ""),), schema=Schema.FIXED).define(recipes=[
		CraftingShapedRecipe(result_count=4, category="building", shape=["X", "#"], ingredients={"X": Ingr("lignite"), "#": Ingr("steel_stick")}),
	])
	OriginalBlock(
		id="lignite_wall_torch", host="minecraft:wall_torch", variants=(("lignite_torch", ""),), schema=Schema.LADDER,
		inventory_model="normal_lignite_torch_wall", foreign_drop="minecraft:torch", drops="lignite_torch",
	).define()
	lamps_and_rods()


def lamps_and_rods() -> None:
	""" Lamps (`gt_1`) and rods (`hb_1`), tinted planks hanging from or standing on whatever they touch, lit with flint and steel. """
	for color in COLORS:
		OriginalBlock(
			id=f"{color.name}_rod", host="minecraft:structure_void", variants=(("rod", ""),), schema=Schema.SOLID_NEIGHBOUR,
			inventory_model="rod_inventory", color=color.rgb, interaction=Interaction(width=0.3, height=1.0),
		).define(recipes=[
			CraftingShapedRecipe(result_count=2, category="building", shape=["X", "X"], ingredients={"X": Ingr("minecraft:stick")})
			if color.name == "white" else dyed("white_rod", color),
		])
		OriginalBlock(
			id=f"{color.name}_lamp", host="minecraft:structure_void", variants=(("lamp_off", ""),), schema=Schema.SOLID_NEIGHBOUR,
			inventory_model="lantern", color=color.rgb, interaction=Interaction(width=0.6, height=0.8), tags=(f"lights.{color.name}_lit_lamp",),
		).define(recipes=[
			CraftingShapedRecipe(
				result_count=4, category="building", shape=["XXX", "WYW", "XXX"],
				ingredients={"X": Ingr("white_rod"), "Y": Ingr("minecraft:torch"), "W": Ingr("minecraft:glass")},
			) if color.name == "white" else dyed("white_lamp", color),
		])
		OriginalBlock(
			id=f"{color.name}_lit_lamp", host="minecraft:light[level=15]", variants=(("lamp_on", ""),), schema=Schema.SOLID_NEIGHBOUR,
			inventory_model="lantern", color=color.rgb, interaction=Interaction(width=0.6, height=0.8), drops=f"{color.name}_lamp",
		).define(recipes=[] if color.name == "white" else [dyed("white_lit_lamp", color)])

