""" Blocks of the mod with a behaviour of their own, the behaviours being written by `user.link` from the display tags given here. """
# Imports
from stewbeet import Block, CraftingShapedRecipe, CraftingShapelessRecipe, Ingr, VanillaBlock

from user.definitions.common import COLORS, dyed, lore
from user.original.blocks import Interaction, OriginalBlock, Schema

# Constants
CAMPFIRES: dict[str, str] = {
	"cobblestone": "minecraft:cobblestone",
	"stone": "step_block",
	"brick": "minecraft:bricks",
	"stonebrick": "minecraft:stone_bricks",
	"sandstone": "minecraft:sandstone",
}
""" Campfires (`gf_1`) and the block crafted with flint and steel into 4 of them. """

EFFECT_GENERATORS: list[str] = ["black_smoke", "portal", "explosion", "white_smoke", "lava", "water", "big_black_smoke", "heart"]
""" Particle blocks (`gm_1`), in metadata order. """

FLOWERS: list[str] = ["blue_flower", "white_flower", "black_flower"]


# Functions
def main() -> None:
	OriginalBlock(
		id="box_jump", host="minecraft:oak_planks", variants=(("jumpbox", ""),), schema=Schema.FIXED, inventory_model="jumpbox", tags=("jump_box",),
	).define(manual_category="miscellaneous", components={"lore": lore("Launches whoever stands on it")}, recipes=[
		CraftingShapelessRecipe(category="misc", ingredients=[Ingr("minecraft:oak_planks"), Ingr("ruby")]),
	])
	Block(
		id="box_speed", vanilla_block=VanillaBlock(id="minecraft:oak_planks"), manual_category="miscellaneous",
		components={"lore": lore("Speed when standing on it")},
		recipes=[CraftingShapelessRecipe(category="misc", ingredients=[Ingr("minecraft:oak_planks"), Ingr("sapphire")])],
	)
	OriginalBlock(id="nuclear_bomb", host="minecraft:tnt", variants=(("bombe", ""),), schema=Schema.FIXED, inventory_model="bombe").define(
		manual_category="miscellaneous", components={"lore": lore("Explosion power 12, TNT is 4")},
		recipes=[CraftingShapedRecipe(category="redstone", shape=["###", "###", "###"], ingredients={"#": Ingr("minecraft:tnt")})],
	)
	for name, material in CAMPFIRES.items():
		OriginalBlock(
			id=f"{name}_campfire", host="minecraft:campfire", variants=((f"{name}_fire_camp", ""),), schema=Schema.FIXED,
			inventory_model=f"{name}_fire_camp", foreign_drop="minecraft:charcoal",
		).define(manual_category="miscellaneous", recipes=[CraftingShapelessRecipe(
			result_count=4, category="misc", group="campfire", ingredients=[Ingr(material), Ingr("minecraft:flint_and_steel")],
		)])
	for kind in EFFECT_GENERATORS:
		OriginalBlock(
			id=f"{kind}_effect_generator", host="minecraft:cobblestone", variants=(("effect_generator", ""),), schema=Schema.FIXED,
			inventory_model="effect_generator", tags=(f"effect.{kind}",),
		).define(manual_category="miscellaneous")
	for color in COLORS:
		OriginalBlock(
			id=f"{color.name}_cloud", host="minecraft:structure_void", variants=(("cloud", ""),), schema=Schema.FIXED, inventory_model="cloud",
			color=color.rgb, interaction=Interaction(), tags=("cloud",),
		).define(manual_category="miscellaneous", recipes=[
			CraftingShapedRecipe(
				result_count=8, category="building", shape=["XXX", "X#X", "XXX"],
				ingredients={"X": Ingr("minecraft:white_wool"), "#": Ingr("minecraft:water_bucket")},
			) if color.name == "white" else dyed("white_cloud", color),
		])
	for color in COLORS:
		OriginalBlock(
			id=f"{color.name}_blob", host="minecraft:barrier", variants=(("blob", ""),), schema=Schema.FIXED, inventory_model="blob",
			color=color.rgb, interaction=Interaction(),
		).define(manual_category="miscellaneous", recipes=[] if color.name == "white" else [dyed("white_blob", color)])
	for team in ("blue", "red"):
		OriginalBlock(
			id=f"{team}_block_ctf", host="minecraft:glass", variants=((f"{team}_block_CTF", ""),), schema=Schema.FIXED,
			inventory_model=f"{team}_block_CTF",
		).define(manual_category="miscellaneous", recipes=[CraftingShapedRecipe(
			result_count=8, category="misc", shape=["XXX", "XGX", "XXX"], ingredients={"X": Ingr(f"minecraft:{team}_wool"), "G": Ingr("minecraft:glass")},
		)])
	machines()
	nature()


def machines() -> None:
	OriginalBlock(
		id="iron_furnace", host="minecraft:furnace", variants=(("iron_furnace", "lit=false"), ("lit_iron_furnace", "lit=true")),
		schema=Schema.FURNACE, inventory_model="iron_furnace", tags=("iron_furnace",),
	).define(manual_category="miscellaneous", components={"lore": lore("Cooks twice as fast")}, recipes=[CraftingShapedRecipe(
		category="misc", shape=["XXX", "XFX", "XXX"], ingredients={"X": Ingr("minecraft:iron_ingot"), "F": Ingr("minecraft:furnace")},
	)])
	OriginalBlock(
		id="steel_brewing_stand", host="minecraft:brewing_stand", variants=(("steel_brewing_stand", ""),), schema=Schema.BREWING,
		tags=("steel_brewing_stand",),
	).define(manual_category="miscellaneous", components={"lore": lore("Brews in 12.5 seconds instead of 20")}, recipes=[CraftingShapedRecipe(
		category="misc", shape=[" B ", "###"], ingredients={"B": Ingr("minecraft:blaze_rod"), "#": Ingr("steel_block")},
	)])


def nature() -> None:
	OriginalBlock(id="cherry_cake", host="minecraft:cake", variants=(("cherry_cake", ""),), schema=Schema.CAKE).define(
		manual_category="food", recipes=[CraftingShapedRecipe(category="misc", shape=["X", "#"], ingredients={"X": Ingr("cherry"), "#": Ingr("minecraft:cake")})],
	)
	for flower in FLOWERS:
		OriginalBlock(
			id=flower, host="minecraft:tripwire", variants=((flower, ""),), schema=Schema.FIXED, foreign_drop="minecraft:string", tags=(flower,),
		).define(manual_category="miscellaneous")

