#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/02 23:17:34 by aantela-         #+#    #+#              #
#    Updated: 2026/08/02 23:17:34 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._days = 0
        else:
            self._days = days

        print(f"Plant created: {self}")

    def __str__(self) -> str:
        return f"{self._name}: {self._height}cm, {self._days} days old"

    def show(self) -> None:
        print(self)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = round(float(height), 1)
        val = int(self._height) if self._height.is_integer() else self._height
        print(f"Height updated:{val}cm")
        return True

    def set_age(self, days: int) -> bool:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        self._days = days
        print(f"Age updated: {self._days} days")
        return True

    def grow(self, size: float = 0.0) -> None:
        if size > 0:
            self.set_height(self._height + size)

    def age(self, days: int = 0) -> None:
        if days > 0:
            self.set_age(self._days + days)


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    rose.set_height(25)
    print(f"Current state: {rose}")
    rose.set_age(10)
    print(f"Current state: {rose}")
    rose.set_height(-5)
    rose.set_age(-10)
    print(f"Current state: {rose}")
    rose.show()
