
#> common_signals:v0.1.2/load/confirm_load
#
# @within	common_signals:v0.1.2/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded Common Signals v0.1.2]","color":"green"}
scoreboard players set #common_signals.loaded load.status 1

