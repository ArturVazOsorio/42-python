#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/05 19:12:49 by aantela-         #+#    #+#              #
#    Updated: 2026/11/05 19:12:49 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    if not achievements:
        return set()
    return set(random.sample(achievements,
                             random.randint(1, len(achievements))))


if __name__ == "__main__":
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
    ]
    players_names = ['Alice', 'Bob', 'Charlie', 'Dylan']

    print("=== Achievement Tracker System ===\n")
    players = {name: gen_player_achievements(achievements)
               for name in players_names
               }
    for name, ach_set in players.items():
        print(f"Player {name}: {ach_set}")

    all_distinct = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_distinct}")

    common = set.intersection(*players.values())
    print(f"\nCommon achievements: {common}\n")

    full_pool_set = set(achievements)
    for name, ach_set in players.items():
        others_achievements = set().union(*(s for n, s
                                            in players.items() if n != name))
        only_has = ach_set.difference(others_achievements)

        print(f"\nOnly {name} has: {only_has}", end="")
    print()
    for name, ach_set in players.items():
        missing = full_pool_set.difference(ach_set)
        print(f"\n{name} is missing: {missing}", end="")
    print()
