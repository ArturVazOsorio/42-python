#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/04 07:53:25 by aantela-         #+#    #+#              #
#    Updated: 2026/11/04 08:09:52 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import math


Coords = tuple[float, float, float]


def parse_coords(raw: str) -> Coords:
    parts = [p.strip() for p in raw.split(",")]
    if len(parts) != 3:
        raise ValueError("Invalid syntax")

    values = []
    for part in parts:
        try:
            values.append(float(part))
        except ValueError as e:
            raise ValueError(f"Error on parameter '{part}': {e}") from None

    x, y, z = values
    return (x, y, z)


def get_player_pos():
    while True:
        raw = input("Enter new coordinates as floats in format  'x, y, z':")
        try:
            return parse_coords(raw)
        except ValueError as e:
            print(e)


def main() -> None:
    origin: Coords = (0.0, 0.0, 0.0)

    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {math.dist(origin, pos1):.4f}")
    print()

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{math.dist(pos1, pos2):.4f}"
    )


if __name__ == "__main__":
    main()
