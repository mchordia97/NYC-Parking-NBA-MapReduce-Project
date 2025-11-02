#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

for line in sys.stdin:
    line = line.strip()
    vehicle_body_type = line.split(",")[6]
    vehicle_year = line.split(",")[35]

    if vehicle_body_type != "Vehicle Body Type" and vehicle_year !="Vehicle Year":
        if vehicle_body_type != "" and vehicle_year != "0":
                print('%s\t%s\t%s' % (vehicle_body_type,vehicle_year, 1))
