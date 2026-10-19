""" Functions picking, for a display entity, the model and rotation the original blockstate gives to its host block state. """
# Imports
import json
import math
from dataclasses import dataclass

from stewbeet import write_function
from stouputils.typing import JsonDict

from .blocks import OriginalBlock, Schema
from .models import ORIGINAL, ModelConverter

# Constants
SIDES: dict[str, tuple[int, int, int]] = {
	"north": (0, 0, -1), "east": (1, 0, 0), "south": (0, 0, 1), "west": (-1, 0, 0), "top": (0, 1, 0), "bottom": (0, -1, 0),
}
""" Offset of the neighbour each side property of the neighbour schemas looks at. """

ROTATION_SCORES: dict[Schema, dict[str, int]] = {
	Schema.FACING_AWAY: {"north": 1, "east": 2, "south": 3, "west": 4},
	Schema.FACING_PLAYER: {"south": 1, "west": 2, "north": 3, "east": 4},
}
""" The `#rotation` score StewBeet's get_rotation gives for each `facing`, 1 being a player looking south. """


# Classes
@dataclass(frozen=True)
class Look:
	""" One model of a block and the transformation of the display showing it, shared by every block using the same one. """
	role: int
	""" Index of the model among the block's models, written as the display's custom_model_data string. """
	x: int
	y: int


@dataclass(frozen=True)
class Variant:
	state: tuple[tuple[str, str], ...]
	model: str
	x: int
	y: int


# Functions
def read_variants(block: OriginalBlock, converter: ModelConverter) -> list[Variant]:
	""" Every variant of the block's blockstate files, with its models converted, the first one only for a fixed block. """
	variants: list[Variant] = []
	for file, extra in block.variants:
		data: dict[str, dict[str, JsonDict | list[JsonDict]]] = json.loads((ORIGINAL / "iyc/blockstates" / f"{file}.json").read_text(encoding="utf-8"))
		for key, value in data["variants"].items():
			first: JsonDict = value[0] if isinstance(value, list) else value
			pairs: list[str] = [pair for pair in (*key.split(","), *extra.split(",")) if "=" in pair]
			state = tuple(sorted((prop, value) for prop, _, value in (pair.partition("=") for pair in pairs)))
			if block.schema == Schema.SLOPE:
				if dict(state).get("shape", "straight") != "straight":
					continue
				state = tuple(pair for pair in state if pair[0] != "shape")
			model, x, y = converter.placed(first)
			variants.append(Variant(state=state, model=model, x=x, y=y))
	return variants[:1] if block.schema == Schema.FIXED else variants


def condition(block: OriginalBlock, prop: str, value: str) -> str:
	""" The execute subcommand holding when the display's block has `prop=value`. """
	if block.schema == Schema.SLOPE:
		if prop == "half":
			return f"if score #upper iyc.data matches {int(value == 'top')}"
		return f"if score #rotation iyc.data matches {ROTATION_SCORES[Schema.FACING_PLAYER][value]}"
	if block.schema in ROTATION_SCORES:
		return f"if score #rotation iyc.data matches {ROTATION_SCORES[block.schema][value]}"
	if block.schema in (Schema.SAME_NEIGHBOUR, Schema.SOLID_NEIGHBOUR):
		return f"if score #side_{prop} iyc.data matches {int(value == 'true')}"
	if block.schema == Schema.SLAB:
		return f"if block ~ ~ ~ {block.host_tag}[type={value}]"
	if block.schema == Schema.WALL and prop != "up":
		return f"{'unless' if value == 'true' else 'if'} block ~ ~ ~ {block.host_tag}[{prop}=none]"
	return f"if block ~ ~ ~ {block.host_tag}[{prop}={value}]"


def neighbour_scores(block: OriginalBlock, props: set[str]) -> str:
	""" Commands storing in `#side_<prop>` whether each side connects, before the tree of a neighbour schema reads them. """
	lines: list[str] = []
	for prop in sorted(props):
		dx, dy, dz = SIDES[prop]
		if block.schema == Schema.SAME_NEIGHBOUR:
			test = f"positioned ~{dx - 0.5} ~{dy - 0.5} ~{dz - 0.5} if entity @e[type=item_display,tag=iyc.connect.{block.connects_to},dx=0,dy=0,dz=0]"
		else:
			test = f"unless block ~{dx} ~{dy} ~{dz} #iyc:not_connectable"
		lines.append(f"execute store success score #side_{prop} iyc.data {test}")
	return "\n".join(lines) + "\n"


def quaternion(axis: str, degrees: int) -> str:
	""" A counterclockwise rotation (seen from the positive side of the axis) as an NBT quaternion.

	>>> quaternion("y", 90)
	'[0.0f,0.7071068f,0.0f,0.7071068f]'
	"""
	half: float = math.radians(degrees) / 2
	values: list[float] = [0.0, 0.0, 0.0, math.cos(half)]
	values["xyz".index(axis)] = math.sin(half)
	return "[" + ",".join(f"{round(v, 7) + 0.0}f" for v in values) + "]"


class SyncWriter:
	""" Writes the shared apply functions and one decision tree per distinct blockstate layout. """

	def __init__(self) -> None:
		self.looks: dict[Look, int] = {}
		self.trees: dict[tuple[object, ...], str] = {}

	def tree(self, block: OriginalBlock, variants: list[Variant], roles: list[str]) -> str:
		""" The function picking the look of a display of this block, written once per layout. """
		entries: list[tuple[dict[str, str], int]] = [
			(dict(v.state), self.look(Look(role=roles.index(v.model), x=v.x, y=v.y))) for v in variants
		]
		key = (block.schema, block.host_tag, block.connects_to, tuple((tuple(sorted(s.items())), n) for s, n in entries))
		if key in self.trees:
			return self.trees[key]
		path: str = f"iyc:shapes/{block.schema.value}_{len(self.trees)}"
		self.trees[key] = path
		if len({n for _, n in entries}) == 1:
			write_function(path, f"function iyc:shapes/apply/{entries[0][1]}\n")
			return path
		props: list[str] = sorted({prop for state, _ in entries for prop in state})
		prelude: str = neighbour_scores(block, set(props)) if block.schema in (Schema.SAME_NEIGHBOUR, Schema.SOLID_NEIGHBOUR) else ""
		self.write_node(block, path, entries, props, prelude)
		return path

	def write_node(self, block: OriginalBlock, path: str, entries: list[tuple[dict[str, str], int]], props: list[str], prelude: str = "") -> None:
		""" One level of the tree: a branch per value of the first property, down to the apply function once the look is known.

		Every branch tests its own value, so a state missing from the blockstate keeps the look the display already has.
		"""
		prop, rest = props[0], props[1:]
		lines: list[str] = []
		for value in dict.fromkeys(state[prop] for state, _ in entries):
			subset = [(state, n) for state, n in entries if state[prop] == value]
			looks: set[int] = {n for _, n in subset}
			target: str = f"iyc:shapes/apply/{next(iter(looks))}"
			if len(looks) > 1:
				target = f"{path}/{prop}_{value}"
				self.write_node(block, target, subset, rest)
			lines.append(f"execute {condition(block, prop, value)} run return run function {target}")
		write_function(path, prelude + "\n".join(lines) + "\n")

	def look(self, look: Look) -> int:
		""" The number of a look, writing its apply function the first time it is met. """
		if look in self.looks:
			return self.looks[look]
		number: int = len(self.looks)
		self.looks[look] = number
		# An item display draws its model turned half a turn about Y, which the left rotation undoes
		rotation: str = f"left_rotation:{quaternion('y', 180 - look.y)},right_rotation:{quaternion('x', -look.x)}"
		write_function(f"iyc:shapes/apply/{number}", f"""
execute if score @s iyc.shape matches {number} run return 0
scoreboard players set @s iyc.shape {number}
data merge entity @s {{Rotation:[0.0f,0.0f],item:{{components:{{"minecraft:custom_model_data":{{strings:["{look.role}"]}}}}}},transformation:{{{rotation},translation:[0f,0f,0f],scale:[1f,1f,1f]}}}}
""")
		return number

