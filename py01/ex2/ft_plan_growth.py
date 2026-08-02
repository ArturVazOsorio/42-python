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
    def __init__(self, name: str, height: float, days: float):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, size: float = 0.0) -> None:
        self.height = self.height + size

    def age(self, days: float = 0.0) -> None:
        self.days = self.days + days


if __name__ == "__main__":
    print("=== Garde Plant Growth===")
    plant1 = Plant(name="Rose", height=25.0, days=30)
    plant1.show()

    plant1.grow(5.3)
    plant1.age(10)
    plant1.show()
