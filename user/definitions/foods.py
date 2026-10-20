""" Foods (`eb_2`), drinks (`ht_2`), their ingredients and containers, and the hops crop (`gl_1`). """
# Imports
from dataclasses import dataclass

from stewbeet import (
	BlockAlternative,
	CraftingShapedRecipe,
	CraftingShapelessRecipe,
	GrowingSeed,
	Ingr,
	Item,
	RecipeBase,
	VanillaBlock,
)
from stouputils.typing import JsonDict


# Classes
@dataclass(frozen=True, kw_only=True)
class Food:
	id: str
	nutrition: int
	modifier: float
	""" 1.8 saturation modifier, 26.3 saturation being nutrition x modifier x 2. """
	effect: str = ""
	container: str = ""
	""" Item given back once drunk, which also makes it a drink. """
	recipes: list[RecipeBase]


# Constants
EFFECT_SECONDS: int = 30

DRINK_MODIFIER: float = 0.6
""" `ht_2` drops the modifier it is given, so every drink keeps the 0.6 default of `eb_2`. """

FOODS: list[Food] = [
	Food(id="beer", nutrition=8, modifier=DRINK_MODIFIER, effect="minecraft:nausea", container="beer_mug", recipes=[
		CraftingShapelessRecipe(category="misc", ingredients=[Ingr("beer_mug"), Ingr("hops")]),
	]),
	Food(id="hot_chocolate", nutrition=6, modifier=DRINK_MODIFIER, effect="minecraft:speed", container="can", recipes=[
		CraftingShapedRecipe(category="misc", shape=["X#X", " X "], ingredients={"X": Ingr("minecraft:glass"), "#": Ingr("minecraft:cocoa_beans")}),
	]),
	Food(id="coca", nutrition=6, modifier=DRINK_MODIFIER, effect="minecraft:haste", container="can", recipes=[
		CraftingShapelessRecipe(category="misc", ingredients=[Ingr("caffeine"), Ingr("cola"), Ingr("can")]),
	]),
	Food(id="red_bull", nutrition=5, modifier=DRINK_MODIFIER, effect="minecraft:regeneration", container="can", recipes=[
		CraftingShapelessRecipe(category="misc", ingredients=[Ingr("taurine"), Ingr("caffeine"), Ingr("can")]),
	]),
	Food(id="apple_juice", nutrition=4, modifier=DRINK_MODIFIER, effect="minecraft:jump_boost", container="empty_glass", recipes=[
		CraftingShapelessRecipe(category="misc", ingredients=[Ingr("empty_glass"), Ingr("minecraft:apple")]),
	]),
	Food(id="toast", nutrition=2, modifier=1.0, recipes=[
		CraftingShapedRecipe(result_count=4, category="misc", shape=["###"], ingredients={"#": Ingr("minecraft:bread")}),
	]),
	Food(id="nutella", nutrition=10, modifier=1.0, recipes=[
		CraftingShapedRecipe(
			category="misc", shape=["X X", "X#X", " X "], ingredients={"X": Ingr("minecraft:glass"), "#": Ingr("minecraft:cocoa_beans")},
		),
	]),
	Food(id="nutella_toast", nutrition=14, modifier=1.0, recipes=[
		CraftingShapedRecipe(result_count=2, category="misc", shape=["#", "X"], ingredients={"#": Ingr("nutella"), "X": Ingr("toast")}),
	]),
	Food(id="cherry", nutrition=3, modifier=1.0, recipes=[]),
]

CONTAINERS: list[tuple[str, CraftingShapedRecipe]] = [
	("beer_mug", CraftingShapedRecipe(result_count=4, category="misc", shape=["# #", "# #", "###"], ingredients={"#": Ingr("minecraft:glass")})),
	("can", CraftingShapedRecipe(result_count=4, category="misc", shape=["X X", "X X", " X "], ingredients={"X": Ingr("minecraft:iron_ingot")})),
	("empty_glass", CraftingShapedRecipe(result_count=4, category="misc", shape=["# #", "# #", " # "], ingredients={"#": Ingr("minecraft:glass")})),
]


# Functions
def main() -> None:
	for item in ("caffeine", "cola", "hops", "taurine"):
		Item(id=item, manual_category="material")
	for container, recipe in CONTAINERS:
		Item(id=container, manual_category="material", recipes=[recipe])
	for food in FOODS:
		components: JsonDict = {"food": {
			"nutrition": food.nutrition, "saturation": round(food.nutrition * food.modifier * 2, 2), "can_always_eat": bool(food.container),
		}}
		if food.container:
			components["max_stack_size"] = 1
			components["consumable"] = {"animation": "drink", "sound": "minecraft:entity.generic.drink", "on_consume_effects": [
				{"type": "minecraft:apply_effects", "effects": [{"id": food.effect, "duration": EFFECT_SECONDS * 20, "amplifier": 0}]},
			]}
		Item(id=food.id, manual_category="food", components=components, recipes=food.recipes, remainder=food.container or None)
	BlockAlternative(
		id="hops_seeds", vanilla_block=VanillaBlock(id="minecraft:wheat"), manual_category="material",
		growing_seed=GrowingSeed(texture_basename="hops", seconds=480, planted_on="farmland", loots="iyc:seeds/hops"),
		recipes=[CraftingShapedRecipe(
			result_count=4, category="building", shape=["#", "W", "V"], result=Ingr("minecraft:grass_block"),
			ingredients={"#": Ingr("minecraft:water_bucket"), "W": Ingr("hops_seeds"), "V": Ingr("minecraft:dirt")},
		)],
	)

