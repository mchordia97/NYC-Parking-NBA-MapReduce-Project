#!/usr/bin/python
from operator import itemgetter
import sys

dict_color_count = {}

for line in sys.stdin:
    line = line.strip()
    vehicle_color,num = line.split('\t')
    try:
        num = int(num)
        dict_color_count[vehicle_color] = dict_color_count.get(vehicle_color, 0) + num
    except ValueError:
        pass
largest = sorted(dict_color_count.items(), key=itemgetter(1))[-1]

print('%s\t%s' % (largest))
