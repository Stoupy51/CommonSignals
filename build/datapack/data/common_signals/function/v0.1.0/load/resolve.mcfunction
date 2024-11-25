
#> common_signals:v0.1.0/load/resolve
#
# @within	#common_signals:resolve
#

# If correct version, load the datapack
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 1 if score #common_signals.patch load.status matches 0 run function common_signals:v0.1.0/load/main

