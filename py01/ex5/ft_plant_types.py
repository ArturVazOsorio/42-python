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
    def __init__(self, name: str, height: float = 0.0, days: int = 0) -> None:
        self.name = name
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
        if days < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._days = 0
        else:
            self._days = int(days)

        print(f"Plant created: {self}")

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.day} days old")

    def show(self) -> None:
        print(self)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = round(float(height), 1)
        val = int(self._height) if self._height % 1 == 0 else self._height
        print(f"Height updated: {val}cm")
        return True

    def set_age(self, days: int) -> bool:
        if days < 0:
            print(f"{self.name}: Error. age can't be negative")
            print("Age update rejected")
            return False
        self._days = days
        print(f"Age updated : {self._days} days")
        return True

    def grow (self)


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    rose.show()
