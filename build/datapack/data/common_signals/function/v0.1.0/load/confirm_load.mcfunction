
#> common_signals:v0.1.0/load/confirm_load
#
# @within	common_signals:v0.1.0/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded Common Signals v0.1.0]","color":"green"}
scoreboard players set #common_signals.loaded load.status 1

