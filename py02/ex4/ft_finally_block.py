#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_finally_block.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/10/26 12:39:13 by aantela-         #+#    #+#              #
#    Updated: 2026/10/26 12:58:31 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


# class WaterError(GardenError):#
#    def __int__(self, message: str = "Unknown water error") -> None:#
#        super().__init__(message)#


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to Water:'{plant_name}'")
    print(f"Watering {plant_name} [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n...ending test and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("\nClenup always happens, even with errors!")
