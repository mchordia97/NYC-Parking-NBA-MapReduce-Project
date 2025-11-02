#!/usr/bin/python
from operator import itemgetter
import sys

dict_type_count = {}
for line in sys.stdin:
    line = line.strip()
    vehicle_body_type,vehicle_year,num = line.split('\t')
    try:
        keys=(vehicle_body_type,vehicle_year)
        num = int(num)
        dict_type_count[keys] = dict_type_count.get(keys, 0) + num

    except ValueError:
        pass

top_pair = sorted(dict_type_count.items(), key=itemgetter(1))[-1]
print('%s\t%s' %(top_pair))
