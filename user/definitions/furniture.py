""" Furniture of the mod in its 4 materials: tables, little tables, stools, high stools, benches and chairs, plus the shelf and the barrel. """
# Imports
from dataclasses import dataclass

from stewbeet import CraftingShapedRecipe, Ingr

from user.original.blocks import Interaction, OriginalBlock, Schema


# Classes
@dataclass(frozen=True, kw_only=True)
class Material:
	name: str
	ingredient: str


@dataclass(frozen=True, kw_only=True)
class Furniture:
	name: str
	schema: Schema
	interaction: Interaction
	shape: list[str]
	""" Recipe shape, `X` being the material and `#` sticks. """
	connects: bool = False


# Constants
MATERIALS: list[Material] = [
	Material(name="oak",         ingredient="minecraft:oak_planks"),
	Material(name="birch",       ingredient="minecraft:birch_planks"),
	Material(name="cobblestone", ingredient="minecraft:cobblestone"),
	Material(name="stone",       ingredient="minecraft:stone"),
]
""" Materials of `gy_1`. The jar crafts stone furniture from stone meta 1 (granite in 1.8), read here as plain stone. """

FURNITURE: list[Furniture] = [
	Furniture(name="table",        schema=Schema.SAME_NEIGHBOUR, interaction=Interaction(height=0.85), shape=["XXX", "# #", "# #"], connects=True),
	Furniture(name="little_table", schema=Schema.SAME_NEIGHBOUR, interaction=Interaction(height=0.38), shape=["XXX", "# #"], connects=True),
	Furniture(name="stool",        schema=Schema.FIXED,          interaction=Interaction(seat=0.59),   shape=["XX", "##"]),
	Furniture(name="high_stool",   schema=Schema.FIXED,          interaction=Interaction(seat=0.875),  shape=["XX", "##", "##"]),
	Furniture(name="bench",        schema=Schema.SAME_NEIGHBOUR, interaction=Interaction(seat=0.59),   shape=["XXX", "###"], connects=True),
	Furniture(name="chair",        schema=Schema.FACING_AWAY,    interaction=Interaction(seat=0.5),    shape=["  X", "XXX", "# #"]),
]
""" Tables keep their interaction under the top, so blocks can still be placed on them. """


# Functions
def main() -> None:
	for furniture in FURNITURE:
		for material in MATERIALS:
			name: str = f"{material.name}_{furniture.name}"
			OriginalBlock(
				id=name, host="minecraft:barrier", variants=((name, ""),), schema=furniture.schema,
				inventory_model=f"item/{name}" if furniture.name == "bench" else name,
				connects_to=furniture.name if furniture.connects else "", interaction=furniture.interaction,
			).define(manual_category="furniture", recipes=[CraftingShapedRecipe(
				category="building", group=furniture.name, shape=furniture.shape,
				ingredients={"X": Ingr(material.ingredient), "#": Ingr("minecraft:stick")},
			)])
	OriginalBlock(
		id="oak_shelf", host="minecraft:barrier", variants=(("oak_shelf", ""),), schema=Schema.FACING_PLAYER,
		inventory_model="oak_shelf", interaction=Interaction(),
	).define(manual_category="furniture", recipes=[CraftingShapedRecipe(
		result_count=2, category="building", shape=["XXX", "X X", "X X"], ingredients={"X": Ingr("minecraft:oak_planks")},
	)])
	OriginalBlock(
		id="oak_barrel", host="minecraft:barrel", variants=(("barrel", ""),), schema=Schema.FIXED, inventory_model="oak_barrel",
	).define(manual_category="furniture", recipes=[CraftingShapedRecipe(
		result_count=4, category="misc", shape=["XXX", "###", "XXX"],
		ingredients={"X": Ingr("minecraft:oak_planks"), "#": Ingr("minecraft:iron_ingot")},
	)])
	OriginalBlock(
		id="flatware", host="minecraft:tripwire", variants=(("flatware", ""),), schema=Schema.FIXED, foreign_drop="minecraft:string",
	).define(manual_category="furniture", recipes=[CraftingShapedRecipe(
		result_count=2, category="misc", shape=["X#X", "X#X"], ingredients={"X": Ingr("minecraft:iron_ingot"), "#": Ingr("minecraft:glass")},
	)])

