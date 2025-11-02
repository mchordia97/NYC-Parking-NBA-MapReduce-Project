#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

player_fear_scores = {}

# Count how many missed and made shots for each player for each defender
for line in sys.stdin:
    player_name, defender_name, shot_result, count = line.split('\t')

    if player_name not in player_fear_scores:
        player_fear_scores[player_name] = {defender_name: [0, 0]}
    elif defender_name not in player_fear_scores[player_name]:
        player_fear_scores[player_name][defender_name] = [0, 0]

        # Increment number of made shots only if this shot was made
    if shot_result == 'made':
        player_fear_scores[player_name][defender_name][0] += int(count)
    # Increment number of total shots
    player_fear_scores[player_name][defender_name][1] += int(count)

# For each player, get the "most unwanted defender" (most number of missed shots)
for player in player_fear_scores:
    # Maximize the number of missed shots
    least_successful_attempts = sorted(player_fear_scores[player].items(), key=lambda x: x[1][1] - x[1][0], reverse=True)
    most_unwanted = least_successful_attempts[0]

    print ('%s\t%s\t(%s/%s shots made)' % (player, most_unwanted[0], most_unwanted[1][0], most_unwanted[1][1]))
