# Imports
from dataclasses import dataclass

from stewbeet import CraftingShapedRecipe, Ingr
from stouputils.typing import JsonDict


# Classes
@dataclass(frozen=True, kw_only=True)
class Color:
	name: str
	rgb: int
	""" Map color the mod tints its colored blocks with (`gk_1.F`). """

	@property
	def dye(self) -> str:
		return f"minecraft:{self.name}_dye"


# Constants
COLORS: list[Color] = [
	Color(name="white",      rgb=0xFFFFFF),
	Color(name="orange",     rgb=0xD87F33),
	Color(name="magenta",    rgb=0xB24CD8),
	Color(name="light_blue", rgb=0x6699D8),
	Color(name="yellow",     rgb=0xE5E533),
	Color(name="lime",       rgb=0x7FCC19),
	Color(name="pink",       rgb=0xF27FA5),
	Color(name="gray",       rgb=0x4C4C4C),
	Color(name="light_gray", rgb=0x999999),
	Color(name="cyan",       rgb=0x4C7F99),
	Color(name="purple",     rgb=0x7F3FB2),
	Color(name="blue",       rgb=0x334CB2),
	Color(name="brown",      rgb=0x664C33),
	Color(name="green",      rgb=0x667F33),
	Color(name="red",        rgb=0x993333),
	Color(name="black",      rgb=0x191919),
]
""" The 16 colors in wool metadata order. """


# Functions
def lore(text: str) -> list[JsonDict]:
	return [{"text": text, "color": "gray", "italic": False}]


def dyed(white_id: str, color: Color) -> CraftingShapedRecipe:
	""" The mod's coloring recipe (`gk_1.c`): 8 white blocks around a dye give 8 blocks of its color. """
	return CraftingShapedRecipe(
		result_count=8, category="building", shape=["###", "#D#", "###"], ingredients={"#": Ingr(white_id), "D": Ingr(color.dye)},
	)

