# Imports
from stewbeet import (
	Context,
	Item,
	Mem,
	Painting,
	PaintingData,
	add_item_model_component,
	add_item_name_and_lore_if_missing,
	add_private_custom_data_for_namespace,
	add_smithed_ignore_vanilla_behaviours_convention,
	export_all_definitions_to_json,
	generate_custom_records,
)

from user.definitions import building, equipment, foods, furniture, lights, materials, special


# Main function
def beet_default(ctx: Context) -> None:
	materials.main()
	generate_custom_records("auto")
	foods.main()
	equipment.main()
	building.main()
	lights.main()
	furniture.main()
	special.main()
	Painting(id="tele", manual_category="decoration", painting_data=PaintingData(texture="tele", width=3, height=2))

	for item_id in Mem.definitions:
		item = Item.from_id(item_id)
		if not item.manual_category:
			item.manual_category = "miscellaneous"

	add_item_model_component()
	add_item_name_and_lore_if_missing()
	add_private_custom_data_for_namespace()
	add_smithed_ignore_vanilla_behaviours_convention()
	foods.give_back_containers()
	export_all_definitions_to_json(f"{ctx.directory}/database_debug.json")

