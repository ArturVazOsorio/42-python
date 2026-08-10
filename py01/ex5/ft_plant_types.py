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
            self._days = days

    def height(self) -> float:
        return self._height

    def day(self) -> int:
        return self._days

    def __str__(self) -> str:
        return f"{self.name}: {self._height}cm, {self._days} days old"

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

    def grow(self, size: float = 0.0) -> None:
        if size > 0:
            self.set_height(self._height + size)

    def age(self, days: int = 0) -> None:
        if days > 0:
            self.set_age(self._days + days)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days: int = 0,
        color: str = ""
    ) -> None:
        self.color = color
        self._blooming = False
        super().__init__(name, height, days)

    def __str__(self) -> str:
        bloom_status = ("is blooming beautifully!"
                        if self._blooming else "has not bloomed yet")
        return (f"{super().__str__()}\n"
                f"Color: {self.color}\n"
                f"{self.name} {bloom_status}")

    def bloom(self):
        self._blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float = 0.0,
                 days: int = 0, trunk_diameter: int = 0) -> None:
        self.trunk_diameter = float(trunk_diameter)
        super().__init__(name, height, days)

    def __str__(self) -> str:
        return f"{super().__str__()}\nTrunk diameter: {self.trunk_diameter}cm"

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days: int = 0,
        harvest_season: str = ""
    ) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        super().__init__(name, height, days)

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"Harvest season: {self.harvest_season}\n"
                f"Nutritional value: {self.nutritional_value}")

    def age(self, days: int = 0):
        super().age(days)
        if days > 0:
            self.nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()
