#!/usr/bin/python
from operator import itemgetter
import sys

dict_street_count = {}
for line in sys.stdin:
    line = line.strip()
    street_name,num = line.split('\t')
    try:
        num = int(num)
        dict_street_count[street_name] = dict_street_count.get(street_name, 0) + num

    except ValueError:
        pass

largest = sorted(dict_street_count.items(), key=itemgetter(1))[-1]

print('%s\t%s' % (largest))
