
#> common_signals:v0.1.1/load/confirm_load
#
# @within	common_signals:v0.1.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded Common Signals v0.1.1]","color":"green"}
scoreboard players set #common_signals.loaded load.status 1

