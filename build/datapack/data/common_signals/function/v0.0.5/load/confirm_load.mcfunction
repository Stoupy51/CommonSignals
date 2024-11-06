
#> common_signals:v0.0.5/load/confirm_load
#
# @within	common_signals:v0.0.5/load/secondary
#

tellraw @a[tag=convention.debug] {"text":"[Loaded Common Signals v0.0.5]","color":"green"}

scoreboard players set #common_signals.loaded load.status 1

