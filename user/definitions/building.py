""" Building blocks of the mod: full blocks, stairs, slopes, slabs, walls, fences, gates, trapdoors, the glowstone plate and the iron ladder. """
# Imports
from dataclasses import dataclass

from stewbeet import CraftingShapedRecipe, Ingr

from user.definitions.common import COLORS, dyed
from user.original.blocks import Interaction, OriginalBlock, Schema


# Classes
@dataclass(frozen=True, kw_only=True)
class Row:
	""" One block of a family whose blockstate file is named after the block. """
	id: str
	material: str
	host: str = ""
	""" Empty for the slopes, all standing on a barrier. """
	count: int
	hand_drop: bool = False


# Constants
STAIRS: list[Row] = [
	Row(id="log_stairs",                 host="minecraft:oak_stairs",              material="minecraft:oak_log",       count=4),
	Row(id="glowstone_stairs",           host="minecraft:oak_stairs",              material="minecraft:glowstone",     count=4),
	Row(id="iron_stairs",                host="minecraft:waxed_cut_copper_stairs", material="minecraft:iron_ingot",    count=4),
	Row(id="obsidian_stairs",            host="minecraft:stone_stairs",            material="obsidian_ingot",          count=4),
	Row(id="step_stairs",                host="minecraft:stone_stairs",            material="minecraft:smooth_stone_slab", count=4),
	Row(id="slate_stairs",               host="minecraft:stone_stairs",            material="slate",                   count=2),
	Row(id="oak_reversed_planks_stairs", host="minecraft:oak_stairs",              material="reversed_oak_planks",     count=4),
]
""" Stairs (`dc`), crafted from 6 materials in the stairs shape. The wool ones are the 26.3 wool stairs, the glass ones stand on a barrier as the slopes. """

SLOPES: list[Row] = [
	Row(id="stone_slopes",         material="minecraft:stone",         count=4),
	Row(id="slate_slopes",         material="slate",                   count=2),
	Row(id="sandstone_slopes",     material="minecraft:sandstone",     count=2),
	Row(id="glowstone_slopes",     material="minecraft:glowstone",     count=4),
	Row(id="oak_planks_slopes",    material="minecraft:oak_planks",    count=4),
	Row(id="spruce_planks_slopes", material="minecraft:spruce_planks", count=2),
	Row(id="birch_planks_slopes",  material="minecraft:birch_planks",  count=2),
	Row(id="jungle_planks_slopes", material="minecraft:jungle_planks", count=2),
	Row(id="oak_log_slopes",       material="minecraft:oak_log",       count=4),
	Row(id="spruce_log_slopes",    material="minecraft:spruce_log",    count=2),
	Row(id="birch_log_slopes",     material="minecraft:birch_log",     count=2),
	Row(id="jungle_log_slopes",    material="minecraft:jungle_log",    count=2),
	Row(id="glass_slopes",         material="minecraft:glass",         count=2),
]
""" Slopes: stairs blocks with a slope model, crafted from 6 materials in a diagonal both ways, standing on a barrier here since stairs would show through. """

SLABS: list[Row] = [
	Row(id="netherrack",      host="minecraft:nether_brick_slab", material="minecraft:netherrack", count=6),
	Row(id="reversed_planks", host="minecraft:oak_slab",          material="reversed_oak_planks",  count=6),
	Row(id="obsidian",        host="minecraft:stone_slab",        material="minecraft:obsidian",   count=6),
	Row(id="oak_log",         host="minecraft:oak_slab",          material="minecraft:oak_log",    count=6),
	Row(id="glowstone",       host="minecraft:oak_slab",          material="minecraft:glowstone",  count=6),
	Row(id="slate",           host="minecraft:stone_slab",        material="slate_block",          count=6),
]
""" Slabs of `hu_1`, named `<variant>_slab` with a `<variant>_double_slab` blockstate, crafted from 3 materials in a row. """

WALLS: list[Row] = [
	Row(id="oak_log",   host="minecraft:cobblestone_wall", material="minecraft:oak_log",   count=5, hand_drop=True),
	Row(id="stone",     host="minecraft:cobblestone_wall", material="minecraft:stone",     count=5),
	Row(id="oak_plank", host="minecraft:cobblestone_wall", material="minecraft:stick",     count=5, hand_drop=True),
	Row(id="glowstone", host="minecraft:cobblestone_wall", material="minecraft:glowstone", count=5, hand_drop=True),
	Row(id="slate",     host="minecraft:cobblestone_wall", material="slate_block",         count=5),
]
""" Walls of `hk_1` without a 26.3 equivalent, crafted from 6 materials in two rows (sticks for the plank wall, as the jar says). """

FENCES: list[Row] = [
	Row(id="glowstone", host="minecraft:oak_fence",          material="minecraft:glowstone",  count=6),
	Row(id="log",       host="minecraft:oak_fence",          material="minecraft:oak_log",    count=2),
	Row(id="stone",     host="minecraft:nether_brick_fence", material="minecraft:stone",      count=2),
]
""" Fences (`ar`), sticks around two materials. """

GATES: list[Row] = [
	Row(id="glowstone", host="minecraft:oak_fence_gate", material="minecraft:glowstone",  count=2),
	Row(id="log",       host="minecraft:oak_fence_gate", material="minecraft:oak_log",    count=2),
	Row(id="stone",     host="minecraft:oak_fence_gate", material="minecraft:stone",      count=2),
	Row(id="iron",      host="minecraft:oak_fence_gate", material="minecraft:iron_ingot", count=2),
]
""" Fence gates (`as`), stone sticks around two materials. """

TRAPDOORS: list[Row] = [
	Row(id="stone",     host="minecraft:oak_trapdoor", material="minecraft:stone",     count=4),
	Row(id="glowstone", host="minecraft:oak_trapdoor", material="minecraft:glowstone", count=4),
]
""" Trapdoors (`dx`), opened by hand as their 1.8 material allows, a stone stick and 2 materials. """

WOODS: list[str] = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "cherry"]
""" Reversed planks variants of `bi_0`, crafted from 2 logs side by side into 8. """


# Functions
def main() -> None:
	full_blocks()
	shaped_blocks()
	connected_blocks()


def full_blocks() -> None:
	for wood in WOODS:
		OriginalBlock(
			id=f"reversed_{wood}_planks", host=f"minecraft:{wood}_planks", variants=((f"{wood}_reversed_planks", ""),),
			schema=Schema.FIXED, inventory_model=f"{wood}_reversed_planks",
		).define(recipes=[CraftingShapedRecipe(
			result_count=8, category="building", group="reversed_planks", shape=["##"], ingredients={"#": Ingr(f"minecraft:{wood}_log")},
		)])
	OriginalBlock(
		id="step_block", host="minecraft:smooth_stone", variants=(("step_block", ""),), schema=Schema.FIXED, inventory_model="step_block",
	).define(recipes=[CraftingShapedRecipe(
		result_count=5, category="building", shape=["XXX", "XXX", "XXX"], ingredients={"X": Ingr("minecraft:smooth_stone_slab")},
	)])
	OriginalBlock(
		id="clear_glass", host="minecraft:glass", variants=(("clear_glass", ""),), schema=Schema.FIXED, inventory_model="clear_glass",
	).define(recipes=[CraftingShapedRecipe(
		result_count=4, category="building", shape=["XXX", "XXX", "XXX"], ingredients={"X": Ingr("minecraft:glass")},
	)])


def shaped_blocks() -> None:
	for row in STAIRS:
		OriginalBlock(
			id=row.id, host=row.host, variants=((row.id, ""),), schema=Schema.STAIRS, inventory_model=row.id,
		).define(recipes=[CraftingShapedRecipe(
			result_count=row.count, category="building", shape=["#  ", "## ", "###"], ingredients={"#": Ingr(row.material)},
		)])
	OriginalBlock(
		id="glass_stairs", host="minecraft:barrier", variants=(("glass_stairs", ""),), schema=Schema.SLOPE, inventory_model="glass_stairs",
		interaction=Interaction(), tags=("step",),
	).define(recipes=[CraftingShapedRecipe(
		result_count=4, category="building", shape=["#  ", "## ", "###"], ingredients={"#": Ingr("minecraft:glass")},
	)])
	OriginalBlock(
		id="glass_slab", host="minecraft:barrier", variants=(("glass_slab", ""),), schema=Schema.SLOPE, inventory_model="half_slab_glass",
		interaction=Interaction(), tags=("step",),
	).define(recipes=[CraftingShapedRecipe(result_count=3, category="building", shape=["###"], ingredients={"#": Ingr("minecraft:glass")})])
	for row in SLOPES:
		OriginalBlock(
			id=row.id, host="minecraft:barrier", variants=((row.id, ""),), schema=Schema.SLOPE, inventory_model=row.id,
			interaction=Interaction(), tags=("step",),
		).define(recipes=[
			CraftingShapedRecipe(result_count=row.count, category="building", shape=shape, ingredients={"#": Ingr(row.material)})
			for shape in (["  #", " # ", "###"], ["#  ", " # ", "###"])
		])
	for row in SLABS:
		OriginalBlock(
			id=f"{row.id}_slab", host=row.host, variants=((f"{row.id}_slab", ""), (f"{row.id}_double_slab", "half=double")),
			schema=Schema.SLAB, inventory_model=f"half_slab_{row.id}",
		).define(recipes=[CraftingShapedRecipe(result_count=row.count, category="building", shape=["###"], ingredients={"#": Ingr(row.material)})])
	for row in TRAPDOORS:
		OriginalBlock(
			id=f"{row.id}_trapdoor", host=row.host, variants=((f"{row.id}_trapdoor", ""),), schema=Schema.TRAPDOOR,
			inventory_model=f"{row.id}_trapdoor_bottom",
		).define(recipes=[CraftingShapedRecipe(
			result_count=row.count, category="redstone", shape=["#XX"], ingredients={"#": Ingr("stone_stick"), "X": Ingr(row.material)},
		)])
	OriginalBlock(
		id="glowstone_pressure_plate", host="minecraft:stone_pressure_plate", variants=(("glowstone_pressure_plate", ""),),
		schema=Schema.PLATE, inventory_model="glowstone_pressure_plate_inventory", hand_drop=True,
	).define(recipes=[CraftingShapedRecipe(result_count=3, category="redstone", shape=["##"], ingredients={"#": Ingr("minecraft:glowstone")})])
	OriginalBlock(id="iron_ladder", host="minecraft:ladder", variants=(("iron_ladder", ""),), schema=Schema.LADDER).define(recipes=[
		CraftingShapedRecipe(result_count=6, category="building", shape=["# #", "###", "# #"], ingredients={"#": Ingr("minecraft:iron_ingot")}),
	])


def connected_blocks() -> None:
	for row in WALLS:
		OriginalBlock(
			id=f"{row.id}_wall", host=row.host, variants=((f"{row.id}_wall", ""),), schema=Schema.WALL,
			inventory_model=f"{row.id}_wall_inventory", hand_drop=row.hand_drop,
		).define(recipes=[CraftingShapedRecipe(result_count=row.count, category="building", shape=["###", "###"], ingredients={"#": Ingr(row.material)})])
	for row in FENCES:
		OriginalBlock(
			id=f"{row.id}_fence", host=row.host, variants=((f"{row.id}_fence", ""),), schema=Schema.FENCE,
			inventory_model=f"{row.id}_fence_inventory",
		).define(recipes=[CraftingShapedRecipe(
			result_count=row.count, category="building", shape=["X#X", "X#X"], ingredients={"X": Ingr("minecraft:stick"), "#": Ingr(row.material)},
		)])
	for color in COLORS:
		OriginalBlock(
			id=f"{color.name}_iron_fence", host="minecraft:nether_brick_fence", variants=(("iron_fence", ""),), schema=Schema.FENCE,
			inventory_model="iron_fence_inventory", color=color.rgb,
		).define(recipes=[
			CraftingShapedRecipe(
				result_count=2, category="building", shape=["X#X", "X#X"],
				ingredients={"X": Ingr("minecraft:stick"), "#": Ingr("minecraft:iron_ingot")},
			) if color.name == "white" else dyed("white_iron_fence", color),
		])
	for row in GATES:
		OriginalBlock(
			id=f"{row.id}_fence_gate", host=row.host, variants=((f"{row.id}_fence_gate", ""),), schema=Schema.GATE,
			inventory_model=f"{row.id}_fence_gate_closed",
		).define(recipes=[CraftingShapedRecipe(
			result_count=row.count, category="redstone", shape=["#W#", "#W#"], ingredients={"#": Ingr("stone_stick"), "W": Ingr(row.material)},
		)])

