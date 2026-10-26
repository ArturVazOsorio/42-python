#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/10/26 11:53:20 by aantela-         #+#    #+#              #
#    Updated: 2026/10/26 12:11:42 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_custom_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The Tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught Water Error: {e}")
    print()
    print("Testing catching all garden erros...")
    for test in (
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ):
        try:
            raise test
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_error()
    print("\nAll custom error types work correctly!")
