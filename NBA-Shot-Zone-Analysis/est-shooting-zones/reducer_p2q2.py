#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
from operator import itemgetter
from collections import defaultdict
from math import sqrt
hitpoint={}
for line in sys.stdin:
    line = line.strip()
    try:
        point,player,hit=line.split('\t')
        hit=int(hit)
        y=player+'|'+point
        b=hitpoint.get(y,[0,0])
        b[0]=b[0]+hit
        b[1]=b[1]+1
        hitpoint[y]= b
    except ValueError:
          pass

dict={}
for key, value in hitpoint.items():
    y=float(value[0])/float(value[1])
    dict[key] = y



player_dict={}

for key, value in dict.items():
    rate=value
    player,point=key.split("|")
    try:
        sec_dict={}
        rate=float(rate)
        sec_dict[point]=sec_dict.get(point,rate)
        b=player_dict.get(player,{})
        b[point]=sec_dict[point]
        player_dict[player]=b
    except ValueError:
        pass


for key,sec in player_dict.items():
    max_value=max(sec.values())
    for m,n in sec.items():
        if n==max_value:
            print('%s\t\t%s%s'%(key,n*100,' %'))

