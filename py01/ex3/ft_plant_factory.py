#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/02 22:01:19 by aantela-         #+#    #+#              #
#    Updated: 2026/08/02 22:01:19 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.days} days old")

    def show(self) -> None:
        print(self)

    def grow(self, size: float = 0.0) -> None:
        self.height = round(self.height + size, 1)

    def age(self, days: int = 0) -> None:
        self.days += days


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")
