""" Weapons and special items: crossbow and bolts (`hu_2`), the wands of `fl_1` used by the server plugins, and the datapack's own items. """
# Imports
from stewbeet import CraftingShapedRecipe, CraftingShapelessRecipe, Ingr, Item, RangedWeapon

from user.definitions.common import lore

# Constants
WANDS: list[str] = [
	"baguette_bleue", "baguette_rouge", "baguette_violette", "baguette_jaune", "baguette_verte", "baguette_orange", "screwdriver", "l118a", "sw1911",
]
""" Items of the BAGUETTE tier: 2000 durability, 2 lost per hit, no block they mine faster. """


# Functions
def main() -> None:
	Item(
		id="crossbow", base_item="minecraft:crossbow", manual_category="equipment",
		components={"max_damage": 199}, ranged_weapon=RangedWeapon(charge_time=2.5, damage_multiplier=1.5, ammunition="bolt"),
		recipes=[CraftingShapedRecipe(
			category="equipment", shape=[" #X", "#WX", " #X"],
			ingredients={"X": Ingr("minecraft:string"), "#": Ingr("steel_stick"), "W": Ingr("minecraft:diamond")},
		)],
	)
	Item(
		id="bolt", base_item="minecraft:arrow", manual_category="equipment", components={"lore": lore("x1.5 damage arrow")},
		recipes=[CraftingShapedRecipe(
			result_count=4, category="equipment", shape=["X", "#", "Y"],
			ingredients={"X": Ingr("minecraft:flint"), "#": Ingr("steel_stick"), "Y": Ingr("minecraft:feather")},
		)],
	)
	for wand in WANDS:
		Item(id=wand, manual_category="equipment", components={
			"max_stack_size": 1, "max_damage": 2000, "weapon": {"item_damage_per_attack": 2},
		})
	Item.from_id("l118a").recipes.append(CraftingShapedRecipe(
		category="equipment", shape=["X  ", " XX", " XS"], ingredients={"X": Ingr("steel_ingot"), "S": Ingr("slate")},
	))
	Item.from_id("sw1911").recipes.append(CraftingShapedRecipe(
		category="equipment", shape=["SX ", "  X", " X "], ingredients={"X": Ingr("steel_ingot"), "S": Ingr("slate")},
	))
	for item in ("pokeball", "coin", "hns_item", "quiver", "old_ruby", "blank"):
		Item(id=item, manual_category="miscellaneous")
	Item(
		id="helice_hat", base_item="minecraft:leather_helmet", manual_category="equipment",
		components={
			"lore": lore("A hat that makes you fly"),
			"attribute_modifiers": [{"type": "gravity", "amount": -0.09, "operation": "add_value", "slot": "head", "id": "iyc:gravity.head"}],
		},
		recipes=[CraftingShapelessRecipe(category="equipment", ingredients=[Ingr("minecraft:iron_ingot"), Ingr("minecraft:elytra")])],
	)
	Item(id="rock", base_item="minecraft:snowball", manual_category="miscellaneous", components={"max_stack_size": 99, "lore": lore("Can be thrown")})
	chainmail = Item(
		id="chainmail", manual_category="material",
		recipes=[CraftingShapedRecipe(result_count=6, category="misc", shape=["#", "#"], ingredients={"#": Ingr("minecraft:iron_ingot")})],
	)
	for piece, shape in (("helmet", ["XXX", "X X"]), ("chestplate", ["X X", "XXX", "XXX"]), ("leggings", ["XXX", "X X", "X X"]), ("boots", ["X X", "X X"])):
		chainmail.recipes.append(CraftingShapedRecipe(
			category="equipment", shape=shape, ingredients={"X": Ingr("chainmail")}, result=Ingr(f"minecraft:chainmail_{piece}"),
		))

