#!/usr/bin/python
from operator import itemgetter
import sys

dict_violationtime_count = {}

for line in sys.stdin:
    line = line.strip()
    try:
        #split the line into violationtime and 1
        violationtime,num = line.split()
        num = int(num)

        dict_violationtime_count[violationtime] = dict_violationtime_count.get(violationtime, 0) + num

    except ValueError:
        pass

most_common = sorted(dict_violationtime_count.items(),key=itemgetter(1),reverse=True)[0]
print('%s\t%s' % (most_common))
