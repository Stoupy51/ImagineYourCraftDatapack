""" Turn the mod's 1.8 block models into 26.3 models, with the vanilla 1.8 models they inherit from copied next to them. """
# Imports
import json
from pathlib import Path

from stewbeet import uv_locked
from stouputils.typing import JsonDict

# Constants
ORIGINAL: Path = Path("assets/original")
""" Blockstates, models and textures copied out of the mod's jar, and the vanilla 1.8 models they use. """

TEXTURE_RENAMES: dict[str, str] = {
	"planks_big_oak": "dark_oak_planks",
	"log_big_oak": "dark_oak_log",
	"log_big_oak_top": "dark_oak_log_top",
	"sandstone_normal": "sandstone",
	"stonebrick": "stone_bricks",
	"brick": "bricks",
	"stone_slab_side": "smooth_stone_slab_side",
	"stone_slab_top": "smooth_stone",
	"torch_on": "torch",
}
""" Vanilla textures whose 1.8 name the prefix rules of `modern_texture` do not cover. """

# Functions
def modern_texture(name: str) -> str:
	""" The 26.3 name of a vanilla 1.8 block texture.

	>>> modern_texture("planks_birch"), modern_texture("log_jungle_top")
	('birch_planks', 'jungle_log_top')
	>>> modern_texture("stone_slab_top"), modern_texture("glowstone")
	('smooth_stone', 'glowstone')
	"""
	if name in TEXTURE_RENAMES:
		return TEXTURE_RENAMES[name]
	if name.startswith("planks_"):
		return f"{name.removeprefix('planks_')}_planks"
	if name.startswith("log_"):
		wood, _, top = name.removeprefix("log_").partition("_")
		return f"{wood}_log" + ("_top" if top else "")
	return name


def model_source(reference: str, in_blockstate: bool) -> tuple[str, Path]:
	""" The 26.3 model id and the source file of a model reference found in a blockstate or as a parent.

	In a 1.8 blockstate `iyc:x` is a model of the mod and a bare `x` a vanilla one, while parents spell out `block/`.
	`iyc:item/x` reads an item model of the mod, for the few inventory models that only exist there.

	>>> model_source("iyc:log_stairs", in_blockstate=True)[0], model_source("stone", in_blockstate=True)[0]
	('iyc:block/log_stairs', 'iyc:block/legacy/stone')
	>>> model_source("iyc:block/table", in_blockstate=False)[0], model_source("block/stairs", in_blockstate=False)[0]
	('iyc:block/table', 'iyc:block/legacy/stairs')
	>>> model_id, source = model_source("iyc:item/oak_bench", in_blockstate=True)
	>>> model_id, source.as_posix()
	('iyc:block/item/oak_bench', 'assets/original/iyc/models/item/oak_bench.json')
	"""
	namespace, _, path = reference.rpartition(":")
	name: str = path if in_blockstate else path.removeprefix("block/")
	if namespace == "iyc":
		folder, _, file = name.rpartition("/")
		return f"iyc:block/{name.lower()}", ORIGINAL / "iyc/models" / (folder or "block") / f"{file}.json"
	return f"iyc:block/legacy/{name}", ORIGINAL / "minecraft/models/block" / f"{name}.json"


def without_comments(obj: JsonDict) -> JsonDict:
	""" Drop the `__comment` keys the model editors of the time left everywhere, as a `json.loads` object hook. """
	return {key: value for key, value in obj.items() if not key.startswith("__")}


class ModelConverter:
	""" Converts models on demand, each once, collecting the textures of the mod they need. """

	def __init__(self) -> None:
		self.models: dict[str, JsonDict] = {}
		self.textures: dict[str, Path] = {}
		""" Texture id to the png of the mod it is copied from. """

	def convert(self, reference: str, in_blockstate: bool) -> str:
		""" Convert a model and its parents, returning its 26.3 id. """
		model_id, source = model_source(reference, in_blockstate)
		if model_id in self.models:
			return model_id
		model: JsonDict = json.loads(source.read_text(encoding="utf-8", errors="replace"), object_hook=without_comments)
		model.pop("display", None)
		model["parent"] = self.convert(model["parent"], in_blockstate=False) if "parent" in model else "minecraft:block/block"
		model["textures"] = {key: self.texture(value) for key, value in model.get("textures", {}).items()}
		self.models[model_id] = model
		return model_id

	def placed(self, entry: JsonDict) -> tuple[str, int, int]:
		""" The converted model of a blockstate variant, and the `x` and `y` rotation the display is left to apply. """
		model_id: str = self.convert(entry["model"], in_blockstate=True)
		x, y = entry.get("x", 0), entry.get("y", 0)
		if entry.get("uvlock") and (x or y):
			return self.uv_locked(model_id, x, y), 0, 0
		return model_id, x, y

	def uv_locked(self, model_id: str, x: int, y: int) -> str:
		""" A converted model turned by a blockstate rotation with `uvlock`, returning the id of the turned copy.

		A display entity turns a model with its textures, so the rotation goes into the model itself instead.
		"""
		locked_id: str = f"{model_id}_x{x}_y{y}"
		model: JsonDict = self.models[model_id]
		while "elements" not in model:
			model = self.models[model["parent"]]
		self.models[locked_id] = {"parent": model_id, "elements": [uv_locked(element, x, y) for element in model["elements"]]}
		return locked_id

	def emissive(self, model_id: str) -> None:
		""" Draw every face of a converted model at full light, its elements copied from the parent defining them. """
		model: JsonDict = self.models[model_id]
		source: JsonDict = model
		while "elements" not in source:
			source = self.models[source["parent"]]
		model["elements"] = [{**element, "light_emission": 15} for element in source["elements"]]

	def texture(self, value: str) -> str:
		""" The 26.3 texture of a 1.8 texture value, `#side` style references being kept. """
		if value.startswith("#"):
			return value
		namespace, _, path = value.rpartition(":")
		name: str = path.removeprefix("blocks/")
		if namespace == "iyc":
			self.textures[f"iyc:block/{name.lower()}"] = ORIGINAL / "iyc/textures/blocks" / f"{name}.png"
			return f"iyc:block/{name.lower()}"
		return f"minecraft:block/{modern_texture(name)}"

