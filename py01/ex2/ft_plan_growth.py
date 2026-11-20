#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plan_growth.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/02 13:13:07 by aantela-         #+#    #+#              #
#    Updated: 2026/08/02 13:13:07 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, size: float = 0.0) -> None:
        self.height = round(self.height + size, 1)

    def age(self, days: int = 0) -> None:
        self.days = self.days + days


if __name__ == "__main__":
    print("=== Garde Plant Growth===")
    plant1 = Plant(name="Rose", height=25.0, days=30)
    plant1.show()

    initial_height = plant1.height
    for x in range(1, 8):
        print(f"=== Day {x} ===")
        plant1.grow(0.8)
        plant1.age(1)
        plant1.show()
    growth_this_week = round(plant1.height - initial_height, 1)
    print(f"Growth this week: {growth_this_week:}cm")
