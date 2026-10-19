""" Vanilla recipes the mod adds at the end of `iu_1`, written as plain recipes since they make vanilla items. """
# Imports
from dataclasses import dataclass

from beet import Recipe
from stewbeet import Mem, set_json_encoder

from user.definitions.common import COLORS


# Classes
@dataclass(frozen=True, kw_only=True)
class Tweak:
	name: str
	result: str
	count: int
	shape: list[str]
	key: dict[str, str]


# Constants
TWEAKS: list[Tweak] = [
	Tweak(name="flint",                  result="minecraft:flint",                  count=1, shape=["#"], key={"#": "minecraft:gravel"}),
	Tweak(name="ender_pearl",            result="minecraft:ender_pearl",            count=1, shape=["##", "##"], key={"#": "minecraft:slime_ball"}),
	Tweak(name="saddle",                 result="minecraft:saddle",                 count=2, shape=["###", "XXX"], key={"#": "minecraft:leather", "X": "minecraft:iron_ingot"}),
	Tweak(name="slime_ball",             result="minecraft:slime_ball",             count=8, shape=["###", "#X#", "###"], key={"#": "minecraft:lime_dye", "X": "minecraft:diamond"}),
	Tweak(name="ice",                    result="minecraft:ice",                    count=4, shape=["#", "X"], key={"#": "minecraft:water_bucket", "X": "minecraft:snow_block"}),
	Tweak(name="snow_block",             result="minecraft:snow_block",             count=1, shape=["XX"], key={"X": "minecraft:snowball"}),
	Tweak(name="cobweb",                 result="minecraft:cobweb",                 count=4, shape=["###", "###", "###"], key={"#": "minecraft:string"}),
	Tweak(name="vine",                   result="minecraft:vine",                   count=8, shape=["XXX", "XVX", "XXX"], key={"X": "#minecraft:leaves", "V": "minecraft:ender_pearl"}),
	Tweak(name="chiseled_stone_bricks",  result="minecraft:chiseled_stone_bricks",  count=4, shape=["###", "# #", "###"], key={"#": "minecraft:stone_bricks"}),
	Tweak(name="cracked_stone_bricks",   result="minecraft:cracked_stone_bricks",   count=4, shape=["###", "#X#", "###"], key={"#": "minecraft:stone_bricks", "X": "minecraft:gunpowder"}),
	Tweak(name="mossy_stone_bricks",     result="minecraft:mossy_stone_bricks",     count=4, shape=["###", "#X#", "###"], key={"#": "minecraft:vine", "X": "minecraft:stone_bricks"}),
	Tweak(name="mossy_cobblestone",      result="minecraft:mossy_cobblestone",      count=4, shape=["###", "#X#", "###"], key={"#": "minecraft:vine", "X": "minecraft:cobblestone"}),
	Tweak(name="sponge",                 result="minecraft:sponge",                 count=4, shape=["X#X", "#W#", "X#X"], key={"#": "minecraft:string", "X": "#minecraft:wool", "W": "minecraft:yellow_dye"}),
	Tweak(name="red_mushroom_block",     result="minecraft:red_mushroom_block",     count=4, shape=["#X#", "XVX", "#X#"], key={"#": "minecraft:red_mushroom", "X": "minecraft:bone_meal", "V": "#minecraft:wool"}),
	Tweak(name="brown_mushroom_block",   result="minecraft:brown_mushroom_block",   count=4, shape=["#X#", "XVX", "#X#"], key={"#": "minecraft:brown_mushroom", "X": "minecraft:bone_meal", "V": "#minecraft:wool"}),
]
""" The grass block recipe (water bucket, hops seeds, dirt) needs a custom ingredient and lives on the hops seeds. """

COLORED_SAND: list[Tweak] = [
	Tweak(
		name=f"{color.name}_concrete_powder", result=f"minecraft:{color.name}_concrete_powder", count=8,
		shape=["###", "#D#", "###"], key={"#": "minecraft:sand", "D": color.dye},
	) for color in COLORS
]
""" The colored sand of the mod (`ap`): 8 sand around a dye, made into the concrete powder of that color. """


# Functions
def write_tweaks() -> None:
	for tweak in TWEAKS + COLORED_SAND:
		Mem.ctx.data["iyc"].recipes[f"tweaks/{tweak.name}"] = set_json_encoder(Recipe({
			"type": "minecraft:crafting_shaped", "category": "misc", "pattern": tweak.shape, "key": tweak.key,
			"result": {"id": tweak.result, "count": tweak.count},
		}), max_level=3)

