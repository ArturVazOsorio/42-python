#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/04 16:17:17 by aantela-         #+#    #+#              #
#    Updated: 2026/08/04 16:28:45 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float = 0.0, day: int = 0) -> None:
        self.name = name
        self.height = round(float(height), 1)
        self.day = int(day)

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.day} days old")

    def grow(self, size: float = 0.0) -> None:
        self.height = round(self.height + size, 1)

    def days_up(self, days: int = 0) -> None:
        self.day = self.day + days

    def show(self) -> None:
        print(self)


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    rose.show()
