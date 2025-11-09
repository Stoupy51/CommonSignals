
# Imports
from stewbeet import Advancement, Context, FunctionTag, JsonDict, LootTable, set_json_encoder, write_tick_file, write_versioned_function


# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def beet_default(ctx: Context) -> None:
	ns: str = ctx.project_id
	version: str = ctx.project_version
	major, minor, patch = version.split(".")

	# Write tick
	write_tick_file(f"""
# For each new item discovered, run a signal
execute as @e[type=item,tag=!{ns}.checked] run function {ns}:v{version}/technical/on_new_item
""")

	# New signal when block is destroyed, to break any custom blocks at position
	write_versioned_function("destroyed_block", f"""
# Run tick function
function {ns}:v{version}/tick

# Call custom block destroy functions
function #{ns}:signals/custom_block_destroy
""", tags=[f"{ns}:calls/destroyed_block"])
	ctx.data[ns].function_tags["signals/custom_block_destroy"] = set_json_encoder(FunctionTag({"values": []}))


	# Write inventory changed advancement functions
	write_versioned_function("inventory_changed", f"""
advancement revoke @s only {ns}:v{version}/inventory_changed
execute if score #{ns}.major load.status matches {major} if score #{ns}.minor load.status matches {minor} if score #{ns}.patch load.status matches {patch} run function {ns}:v{version}/technical/inventory_changed
""")  # noqa: E501
	write_versioned_function("technical/inventory_changed", f'clear @s *[minecraft:custom_data={{"{ns}":{{"temp":true}}}}]')

	# Write inventory changed advancement
	adv: JsonDict = {"criteria": {"requirement": {"trigger": "minecraft:inventory_changed"}},"rewards": {"function": f"{ns}:v{version}/inventory_changed"}}
	ctx.data[ns].advancements[f"v{version}/inventory_changed"] = set_json_encoder(Advancement(adv), max_level=-1)

	# Write on_new_item function and function tag
	write_versioned_function("technical/on_new_item", f"""
tag @s add {ns}.checked
function #{ns}:signals/on_new_item

# Check if the item is a temporary item and kill it
execute if data entity @s Item.components."minecraft:custom_data".{ns}.temp run kill @s
""")
	ctx.data[ns].function_tags["signals/on_new_item"] = set_json_encoder(FunctionTag({"values": []}))

	## Write loot tables for polished deepslate
	ctx.data[ns].loot_tables["polished_deepslate"] = set_json_encoder(LootTable({
		"type": "minecraft:block",
		"pools": [
			{
				"rolls": 1,
				"entries": [
					{
						"type": "minecraft:item",
						"name": "minecraft:deepslate",
						"functions": [
							{
								"function": "minecraft:set_components",
								"components": {
									"minecraft:item_model": "air",
									"minecraft:custom_data": f"""{{"{ns}":{{"temp":true}}}}"""
								}
							},
							{
								"function": "minecraft:set_components",
								"components": {
									"minecraft:custom_data": f"""{{"{ns}":{{"silk_touch":true,"temp":true}}}}"""
								},
								"conditions": [
									{
										"condition": "minecraft:match_tool",
										"predicate": {
											"predicates": {
												"minecraft:enchantments": [
													{
														"enchantments": "minecraft:silk_touch",
														"levels": {
															"min": 1
														}
													}
												]
											}
										}
									}
								]
							},
							{
								"function": "minecraft:apply_bonus",
								"enchantment": "minecraft:fortune",
								"formula": "minecraft:ore_drops"
							}
						]
					}
				],
				"conditions": [
					{
						"condition": "minecraft:survives_explosion"
					}
				]
			}
		]
	}), max_level=7)
	ctx.data["minecraft"].loot_tables["blocks/polished_deepslate"] = set_json_encoder(LootTable({
		"type": "minecraft:block",
		"pools": [
			{
				"rolls": 1,
				"entries": [
					{
						"type": "minecraft:loot_table",
						"value": "common_signals:polished_deepslate"
					}
				]
			},
			{
				"rolls": 1,
				"bonus_rolls": 0,
				"entries": [
					{
						"type": "minecraft:item",
						"name": "minecraft:polished_deepslate"
					}
				],
				"conditions": [
					{
						"condition": "minecraft:survives_explosion"
					}
				]
			}
		],
		"random_sequence": "minecraft:blocks/polished_deepslate",
		"__smithed__": {
			"rules": [
				{
					"type": "smithed:append",
					"target": "pools[0].entries",
					"source": {
						"type": "smithed:reference",
						"path": "pools[0].entries[0]"
					}
				}
			]
		}
	}), max_level=7)

	pass

