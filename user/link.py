
# Imports
from python_datapack.constants import *
from python_datapack.utils.print import *
from python_datapack.utils.io import *

# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def main(config: dict) -> None:
	database: dict[str, dict] = config["database"]
	namespace: str = config["namespace"]
	version: str = config["version"]
	major, minor, patch = version.split(".")
	functions: str = f"{config['datapack_functions']}/v{version}"
	advancements: str = f"{config['build_datapack']}/data/{namespace}/advancement/v{version}"
	function_tags: str = f"{config['build_datapack']}/data/{namespace}/tags/function"

	# Write tick
	write_to_file(f"{functions}/tick.mcfunction", f"""
# For each new item discovered, run a signal
execute as @e[type=item,tag=!{namespace}.checked] run function {namespace}:v{version}/technical/on_new_item
""")
	

	# Write inventory changed advancement functions
	write_to_file(f"{functions}/inventory_changed.mcfunction", f"""
advancement revoke @s only {namespace}:v{version}/inventory_changed
execute if score #{namespace}.major load.status matches {major} if score #{namespace}.minor load.status matches {minor} if score #{namespace}.patch load.status matches {patch} run function {namespace}:v{version}/technical/inventory_changed
""")
	write_to_file(f"{functions}/technical/inventory_changed.mcfunction", f'clear @s *[minecraft:custom_data={{"{namespace}":{{"temp":true}}}}]')

	# Write inventory changed advancement
	adv: dict = {"criteria": {"requirement": {"trigger": "minecraft:inventory_changed"}},"rewards": {"function": f"{namespace}:v{version}/inventory_changed"}}
	write_to_file(f"{advancements}/inventory_changed.json", super_json_dump(adv, max_level = -1))

	# Write on_new_item function and function tag
	write_to_file(f"{functions}/technical/on_new_item.mcfunction", f"""
tag @s add {namespace}.checked
function #{namespace}:signals/on_new_item

# Check if the item is a temporary item and kill it
execute if data entity @s Item.components."minecraft:custom_data".{namespace}.temp run kill @s
""")
	write_to_file(f"{function_tags}/signals/on_new_item.json", super_json_dump({"values": []}))

	## Write loot tables for polished deepslate
	vanilla_polished_deepslate: dict = {"type":"minecraft:block","pools":[{"rolls":1,"entries":[{"type":"minecraft:loot_table","value":f"{namespace}:polished_deepslate"}]},{"rolls":1,"bonus_rolls":0,"entries":[{"type":"minecraft:item","name":"minecraft:polished_deepslate"}],"conditions":[{"condition":"minecraft:survives_explosion"}]}],"random_sequence":"minecraft:blocks/polished_deepslate","__smithed__":{"rules":[{"type":"smithed:append","target":"pools[0].entries","source":{"type":"smithed:reference","path":"pools[0].entries[0]"}}]}}
	namespace_polished_deepslate: dict = {"type":"minecraft:block","pools":[{"rolls":1,"entries":[{"type":"minecraft:item","name":"minecraft:deepslate","functions":[{"function":"minecraft:set_components","components":{"minecraft:item_model":"air","minecraft:custom_data":f"{{\"{namespace}\":{{\"temp\":true}}}}"}},{"function":"minecraft:set_components","components":{"minecraft:custom_data":f"{{\"{namespace}\":{{\"silk_touch\":true,\"temp\":true}}}}"},"conditions":[{"condition":"minecraft:match_tool","predicate":{"predicates":{"minecraft:enchantments":[{"enchantments":"minecraft:silk_touch","levels":{"min":1}}]}}}]},{"function":"minecraft:apply_bonus","enchantment":"minecraft:fortune","formula":"minecraft:ore_drops"}]}],"conditions":[{"condition":"minecraft:survives_explosion"}]}]}
	write_to_file(f"{config['build_datapack']}/data/{namespace}/loot_table/polished_deepslate.json", super_json_dump(namespace_polished_deepslate, max_level = -1))
	write_to_file(f"{config['build_datapack']}/data/minecraft/loot_table/blocks/polished_deepslate.json", super_json_dump(vanilla_polished_deepslate, max_level = -1))

	pass

