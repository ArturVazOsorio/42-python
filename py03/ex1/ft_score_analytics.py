#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/10/27 19:23:42 by aantela-         #+#    #+#              #
#    Updated: 2026/10/27 19:44:29 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    score: list[int] = []
    for arg in sys.argv[1:]:
        try:
            score.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not score:
        print("No score provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ..."
              )
        return (1)
    print(f"Scores processed: {score}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score:{sum(score)/len(score)}")
    print(f"Hight score:{max(score)}")
    print(f"Low score:{min(score)}")
    print(f"Score range: {max(score) - min(score)}")


main()
