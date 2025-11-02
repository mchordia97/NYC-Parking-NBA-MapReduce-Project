#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import re
for line in sys.stdin:
    line = line.strip()
    line = re.sub(r'"(\D+),(\D+)"',r'\1\2', line)

    defender_name = line.split(",")[-7]

    player_name = line.split(",")[-2]
    shot_result = line.split(",")[-8]

    if defender_name != "CLOSEST_DEFENDER" and player_name != "player_name" and shot_result != "SHOT_RESULT":
        print('%s\t%s\t%s\t%s' % (player_name, defender_name, shot_result, 1))
