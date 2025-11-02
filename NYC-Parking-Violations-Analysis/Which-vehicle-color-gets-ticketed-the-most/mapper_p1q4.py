#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

for line in sys.stdin:
    line = line.strip()
    vehicle_color = line.split(",")[33]
    if vehicle_color != "Vehicle Color":
        if vehicle_color != "":
                print('%s\t%s' % (vehicle_color, '1'))
