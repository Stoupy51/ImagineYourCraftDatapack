""" Blocks drawn with the mod's own 1.8 models: a vanilla host block holding the collision, and an item display holding the look. """
# Imports
from dataclasses import dataclass, field
from enum import StrEnum

from stewbeet import Block, Mem, RecipeBase, VanillaBlock
from stouputils.typing import JsonDict


# Classes
class Schema(StrEnum):
	""" What the variants of a blockstate file are read from, which also tells when the model has to be picked again.

	A string enum, so members still compare equal once beet imports this module again for the next plugin.
	"""
	FIXED = "fixed"
	""" The first variant only, picked once on placement. """
	FACING_AWAY = "facing_away"
	""" `facing` points away from the player who placed it (chairs), picked once on placement. """
	FACING_PLAYER = "facing_player"
	""" `facing` is the direction the player was looking at (shelves), picked once on placement. """
	STAIRS = "stairs"
	SLOPE = "slope"
	""" Variants of straight stairs, slopes or slabs picked once on placement from the player's look and where they clicked, the host being a barrier. """
	SLAB = "slab"
	""" 1.8 `half=bottom|top|double` read from the host `type`. """
	WALL = "wall"
	""" 1.8 `north=true` read as a host side that is not `none`. """
	FENCE = "fence"
	GATE = "gate"
	TRAPDOOR = "trapdoor"
	PLATE = "plate"
	LADDER = "ladder"
	LAMP = "lamp"
	FURNACE = "furnace"
	BREWING = "brewing"
	CAKE = "cake"
	SAME_NEIGHBOUR = "same_neighbour"
	""" Each horizontal side is true when the neighbour is a block of the same `connects_to` family. """
	SOLID_NEIGHBOUR = "solid_neighbour"
	""" Each of the 6 sides is true unless the neighbour is in `#iyc:not_connectable` (lamps and rods). """

	@property
	def follows_host(self) -> bool:
		""" Whether the model depends on a state that changes after placement. """
		return self not in (Schema.FIXED, Schema.FACING_AWAY, Schema.FACING_PLAYER, Schema.SLOPE)


@dataclass(frozen=True, kw_only=True)
class Interaction:
	""" An interaction entity standing in the block, for hosts that cannot be mined or targeted (barrier, structure void, light). """
	width: float = 1.01
	height: float = 1.01
	seat: float | None = None
	""" Height above the block bottom a player sits at when using it, None when it is not a seat. """


@dataclass(frozen=True, kw_only=True)
class OriginalBlock:
	""" A custom block shown with the original models, every instance being listed by `all()`. """
	id: str
	host: str
	variants: tuple[tuple[str, str], ...]
	""" Blockstate files of `assets/original/iyc/blockstates`, each with the state its variants add, ex: ("lit_iron_furnace", "lit=true"). """
	schema: Schema
	inventory_model: str | None = None
	""" Original model shown in the inventory, `legacy/<name>` for a vanilla 1.8 one, None for a flat icon drawn from `assets/textures/<id>.png`. """
	color: int | None = None
	""" Tint of the faces with a tintindex, as an RGB integer. """
	connects_to: str = ""
	interaction: Interaction | None = None
	foreign_drop: str = ""
	""" The vanilla item the host drops instead of itself (`minecraft:string` for tripwire), turned into this block's item. """
	hand_drop: bool = False
	""" The host needs a tool to drop but the original did not, so the item appears anyway when a survival player broke it. """
	drops: str = ""
	""" The item dropped when broken through its interaction, defaults to the block itself. """
	tags: tuple[str, ...] = field(default_factory=tuple[str, ...])
	""" Extra entity tags of the display, read by the behaviours of `user.link`. """

	def __post_init__(self) -> None:
		Mem.ctx.meta.setdefault("iyc_original_blocks", {})[self.id] = self

	@staticmethod
	def all() -> list[OriginalBlock]:
		""" Every original block defined in this build, kept in the context since beet imports each plugin anew. """
		return list(Mem.ctx.meta.get("iyc_original_blocks", {}).values())

	@property
	def host_tag(self) -> str:
		""" Block tag of every host using this schema, the sync functions testing states through it. """
		return f"#iyc:hosts/{self.schema.value}"

	def define(self, recipes: list[RecipeBase] | None = None, manual_category: str = "building", components: JsonDict | None = None) -> Block:
		""" Register the StewBeet block placing this one. """
		facing: bool = self.schema in (Schema.LADDER, Schema.FURNACE)
		turned: bool = self.schema in (Schema.STAIRS, Schema.SLOPE, Schema.GATE, Schema.TRAPDOOR, Schema.FACING_AWAY, Schema.FACING_PLAYER)
		vanilla_block = VanillaBlock(id=self.host, block_facing="player" if facing else False, visual_facing="player" if turned else "none")
		override_model: JsonDict = (
			{"parent": f"iyc:block/{self.inventory_model.lower()}", "textures": None} if self.inventory_model
			else {"parent": "item/generated", "textures": {"layer0": f"iyc:item/{self.id}"}}
		)
		block = Block(
			id=self.id, vanilla_block=vanilla_block, manual_category=manual_category,
			override_model=override_model, recipes=recipes or [], components=components or {},
		)
		if self.color is not None:
			block.components["custom_model_data"] = {"colors": [self.color]}
		return block

