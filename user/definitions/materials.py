""" Gems, ingots, ores, storage blocks, and the tools and armor of the mod's tiers (`dq_2` tools, `dv_2` armor). """
# Imports
from dataclasses import dataclass

from stewbeet import (
	BlastingRecipe,
	Block,
	CraftingShapedRecipe,
	CraftingShapelessRecipe,
	DefaultOre,
	EquipmentsConfig,
	Ingr,
	Item,
	Mining,
	NoSilkTouchDrop,
	SmeltingRecipe,
	VanillaBlock,
	generate_everything_about_these_materials,
)


# Classes
@dataclass(frozen=True, kw_only=True)
class Tier:
	""" A 1.8 tier expressed against the 26.3 diamond one: durability 1561, speed 8, damage bonus 3, enchantability 10. """
	material: str
	base: str
	durability: int
	speed: float
	damage: float
	enchantability: int
	armor_factor: int
	armor: tuple[int, int, int, int]
	""" Armor points of the helmet, chestplate, leggings and boots. """


# Constants
TIERS: list[Tier] = [
	Tier(material="minecraft:emerald",   base="emerald",    durability=1405, speed=7.0,  damage=2.5,  enchantability=15, armor_factor=26, armor=(3, 7, 5, 3)),
	Tier(material="sapphire",            base="sapphire",   durability=1639, speed=9.0,  damage=3.25, enchantability=8,  armor_factor=40, armor=(3, 8, 6, 3)),
	Tier(material="ruby",                base="ruby",       durability=1717, speed=10.0, damage=3.5,  enchantability=8,  armor_factor=46, armor=(3, 8, 6, 3)),
	Tier(material="topaz",               base="topaz",      durability=1795, speed=11.0, damage=3.75, enchantability=6,  armor_factor=53, armor=(4, 8, 6, 4)),
	Tier(material="adamantium_fragment", base="adamantium", durability=1873, speed=12.0, damage=4.0,  enchantability=6,  armor_factor=59, armor=(4, 8, 6, 4)),
]

SMELTING_XP: dict[str, float] = {
	"sapphire": 0.6, "ruby": 0.6, "topaz": 0.6, "adamantium_fragment": 0.4, "steel_ingot": 0.4, "lignite": 0.4, "slate": 0.4,
}
""" Experience of smelting each ore (`it_1`). """

ARMOR_PIECES: tuple[tuple[str, int, int], ...] = (("helmet", 11, 3), ("chestplate", 16, 8), ("leggings", 15, 6), ("boots", 13, 3))
""" Armor piece, its 1.8 durability multiplier, and the diamond armor points 26.3 already gives it. """

GEM_EXPERIENCE: dict[str, int] = {"min": 3, "max": 6}

ORE_DROPS: dict[str, NoSilkTouchDrop] = {
	"ruby_ore":                 NoSilkTouchDrop(id="ruby",                experience=GEM_EXPERIENCE),
	"deepslate_ruby_ore":       NoSilkTouchDrop(id="ruby",                experience=GEM_EXPERIENCE),
	"sapphire_ore":             NoSilkTouchDrop(id="sapphire",            experience=GEM_EXPERIENCE),
	"deepslate_sapphire_ore":   NoSilkTouchDrop(id="sapphire",            experience=GEM_EXPERIENCE),
	"topaz_ore":                NoSilkTouchDrop(id="topaz",               experience=GEM_EXPERIENCE),
	"deepslate_topaz_ore":      NoSilkTouchDrop(id="topaz",               experience=GEM_EXPERIENCE),
	"adamantium_ore":           NoSilkTouchDrop(id="adamantium_fragment", experience=GEM_EXPERIENCE),
	"deepslate_adamantium_ore": NoSilkTouchDrop(id="adamantium_fragment", experience=GEM_EXPERIENCE),
	"lignite_ore":              NoSilkTouchDrop(id="lignite",             experience={"min": 2, "max": 5}),
	"slate_ore":                NoSilkTouchDrop(id="slate",               experience={"min": 3, "max": 5}),
}
""" What the ores giving experience drop without silk touch (`gz_2`). Steel ore drops raw steel and no experience, as it dropped itself. """

STORAGE_HOSTS: dict[str, str] = {
	"adamantium_block": "minecraft:diamond_block",
	"sapphire_block": "minecraft:diamond_block",
	"ruby_block": "minecraft:diamond_block",
	"topaz_block": "minecraft:diamond_block",
	"raw_steel_block": "minecraft:raw_gold_block",
	"steel_block": "minecraft:gold_block",
	"lignite_block": "minecraft:emerald_block",
	"slate_block": "minecraft:emerald_block",
	"massive_obsidian_block": "minecraft:diamond_block",
}
""" Iron level hosts of the storage blocks, the mod's pickaxe (`er_2`) harvesting them from the iron tier on. """


# Functions
def main() -> None:
	generate_everything_about_these_materials({
		**{tier.material: EquipmentsConfig(DefaultOre.DIAMOND, tier.durability, {
			"attack_damage": tier.damage - 3.0, "mining_efficiency": tier.speed - 8.0,
		}) for tier in TIERS},
		"obsidian_ingot": EquipmentsConfig(DefaultOre.DIAMOND, 3902, {"attack_damage": -0.2, "mining_efficiency": -0.2}),
		"steel_ingot": EquipmentsConfig(DefaultOre.IRON, 444, {"mining_efficiency": 0.1}),
		"lignite": None,
		"slate": None,
		"minecraft:stone": None,
	})
	for tier in TIERS:
		apply_tier(tier)
	for ore, drop in ORE_DROPS.items():
		Block.from_id(ore).no_silk_touch_drop = drop
	for item, xp in SMELTING_XP.items():
		for recipe in Item.from_id(item).recipes:
			if isinstance(recipe, SmeltingRecipe | BlastingRecipe):
				recipe.experience = xp

	Item.from_id("stone_stick").recipes = [CraftingShapedRecipe(
		result_count=4, category="misc", shape=["  #", " # ", "#  "], ingredients={"#": Ingr("minecraft:stone")},
	)]
	Block(
		id="massive_obsidian_block", manual_category="material",
		recipes=[CraftingShapedRecipe(category="misc", group="obsidian", shape=["XXX", "XXX", "XXX"], ingredients={"X": Ingr("obsidian_ingot")})],
	)
	for block, host in STORAGE_HOSTS.items():
		Block.from_id(block).vanilla_block = VanillaBlock(id=host)
	for block in (*STORAGE_HOSTS, *(ore for ore in ORE_DROPS if ore != "lignite_ore"), "steel_ore"):
		Block.from_id(block).mining = Mining(level="iron")
	Item.from_id("obsidian_ingot").recipes = [
		CraftingShapelessRecipe(result_count=9, category="misc", group="obsidian", ingredients=[Ingr("massive_obsidian_block")]),
		SmeltingRecipe(category="misc", group="obsidian", experience=0.25, cookingtime=200, ingredient=Ingr("minecraft:obsidian")),
		BlastingRecipe(category="misc", group="obsidian", experience=0.25, cookingtime=100, ingredient=Ingr("minecraft:obsidian")),
	]


def apply_tier(tier: Tier) -> None:
	""" Set the 1.8 armor durability and points, and the enchantability, which the diamond based generation does not know. """
	for (piece, multiplier, diamond_armor), armor_points in zip(ARMOR_PIECES, tier.armor, strict=True):
		item: Item = Item.from_id(f"{tier.base}_{piece}")
		item.components["max_damage"] = tier.armor_factor * multiplier
		item.components["enchantable"] = {"value": tier.enchantability}
		for modifier in item.components["attribute_modifiers"]:
			if modifier["type"] == "armor":
				modifier["amount"] += armor_points - diamond_armor
	for tool in ("sword", "pickaxe", "axe", "shovel", "hoe"):
		Item.from_id(f"{tier.base}_{tool}").components["enchantable"] = {"value": tier.enchantability}

