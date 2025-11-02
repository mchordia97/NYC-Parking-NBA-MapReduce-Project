#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys
from math import sqrt

def getCentroids(filepath):
    centroids = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
                    line = line.strip()
                    coord = line.split(',')

                    centroids.append([float(coord[0]), float(coord[1]),float(coord[2])])
                except ValueError:
                    break
            else:
                break
            line = fp.readline()

    fp.close()
    return centroids


def assign_clusters(coord):
        minimum_dist = 10000000
        cluster_id = None
        for c in centroids:
            distance = sqrt(pow(coord[0]-c[0],2) + pow(coord[1]-c[1],2) + pow(coord[2]-c[2],2))
            if distance <= minimum_dist:
                minimum_dist = distance
                cluster_id = centroids.index(c)

        return cluster_id

centroids = getCentroids('centroids.txt')
players = ['james harden', 'chris paul', 'stephen curry', 'lebron james']
for line in sys.stdin:
    line = re.sub(r'"(\D+),(\D+)"',r'\1\2', line)
    line = line.strip()
    close_def_dist = line.split(",")[-5]
    shot_clock = line.split(",")[9]
    shot_dist = line.split(",")[12]
    player = line.split(",")[-2]
    hit = line.split(",")[-8]
    hit = hit.replace("made","1")
    hit = hit.replace("missed","0")
    if shot_dist != "SHOT_DIST" and close_def_dist != "CLOSE_DEF_DIST" and shot_clock != "SHOT_CLOCK" and player != "player_name":
        if shot_dist != "" and close_def_dist != "" and shot_clock != "":
                if player in players:
                        coord = [float(shot_dist),float(close_def_dist),float(shot_clock)]
                        cluster_id = assign_clusters(coord)
                        print('%s\t%s\t%s'%(centroids[cluster_id],player,hit))

