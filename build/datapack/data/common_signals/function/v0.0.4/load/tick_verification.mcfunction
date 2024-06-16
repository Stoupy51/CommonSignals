
#> common_signals:v0.0.4/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 if score #common_signals.patch load.status matches 4 run function common_signals:v0.0.4/tick

