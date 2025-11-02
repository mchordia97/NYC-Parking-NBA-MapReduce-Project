#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

for line in sys.stdin:
    line = line.strip()
    street_name = line.split(",")[24]
    if street_name != "Street Name":
        if street_name != "":
                print('%s\t%s' % (street_name, '1'))
