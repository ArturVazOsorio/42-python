#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/09 09:26:42 by aantela-         #+#    #+#              #
#    Updated: 2026/11/09 09:45:21 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import random


def main() -> None:
    print("=== Game Data alchemist ===")

    initial_players = ['Alice', 'bob', 'Charlie', 'dylan',
                       'Emma', 'Gregory', 'john', 'kevin', 'Liam ']
    print(f"\nInitial list of players: {initial_players}")

    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"\nNew list with all names capitalized: {all_capitalized}")

    capitalized_only = [name for name in initial_players if name.istitle()]
    print(f"\nNew list of capitalized name only: {capitalized_only}")

    score_dict = {name: random.randint(50, 1000) for name in all_capitalized}
    print(f"\nScore dict: {score_dict}\n")

    total_score = sum(score_dict.values())
    average_score = total_score / len(score_dict)
    print(f"Score average is {average_score:.2f}")

    high_score = {
        name: score
        for name, score in score_dict.items()if score > average_score}
    print(f"High score: {high_score}")


if __name__ == "__main__":
    main()
