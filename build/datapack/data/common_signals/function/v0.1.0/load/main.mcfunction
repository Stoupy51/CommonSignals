
#> common_signals:v0.1.0/load/main
#
# @within	common_signals:v0.1.0/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #common_signals.loaded load.status matches 1 run function common_signals:v0.1.0/load/secondary

