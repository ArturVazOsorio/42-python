#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/10 01:12:06 by aantela-         #+#    #+#              #
#    Updated: 2026/08/10 01:12:06 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float = 0.0, days: int = 0) -> None:
        self.name = name
        self._height = float(height) if height >= 0 else 0.0
        self._days = days if days >= 0 else 0
        self._stats = self._Stats()

    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    def __str__(self) -> str:
        return f"{self.name}: {self._height}cm, {self._days} days old"

    def show(self) -> None:
        self._stats.show_calls += 1
        print(self)

    def grow(self, size: float = 0.0) -> None:
        if size > 0:
            self._height += float(size)
            self._stats.grow_calls += 1

    def age(self, days: int = 0) -> None:
        if days > 0:
            self._days += days
            self._stats.age_calls += 1

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant")


class Flower(Plant):
    def __init__(self, name: str, height: float = 0.0,
                 days: int = 0, color: str = "") -> None:
        self.color = color
        self._blooming = False
        super().__init__(name, height, days)

    def __str__(self) -> str:
        bloom_status = ("is blooming beautifully!"
                        if self._blooming else "has not bloomed yet")
        return (f"{super().__str__()}\n"
                f"Color: {self.color}\n"
                f"{self.name} {bloom_status}")

    def bloom(self) -> None:
        self._blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float = 0.0,
                 days: int = 0, trunk_diameter: float = 0.0) -> None:
        self.trunk_diameter = float(trunk_diameter)
        super().__init__(name, height, days)
        self._stats: Tree._TreeStats = self._TreeStats()

    class _TreeStats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            super().display()
            print(f"{self.shade_calls} shade")

    def __str__(self) -> str:
        return f"{super().__str__()}\nTrunk diameter: {self.trunk_diameter}cm"

    def produce_shade(self) -> None:
        self._stats.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Seed(Flower):
    def __init__(self, name: str, height: float = 0.0,
                 days: int = 0, color: str = "", seeds: int = 0) -> None:
        self.seeds = seeds
        super().__init__(name, height, days, color)

    def __str__(self) -> str:
        return f"{super().__str__()}\nSeeds: {self.seeds}"


class Vegetable(Plant):
    def __init__(self, name: str, height: float = 0.0,
                 days: int = 0, harvest_season: str = "") -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        super().__init__(name, height, days)

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"Harvest season: {self.harvest_season}\n"
                f"Nutritional value: {self.nutritional_value}")

    def age(self, days: int = 0) -> None:
        super().age(days)
        if days > 0:
            self.nutritional_value += days


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? ->"
          f"{Plant.is_older_than_a_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.seeds = 42
    sunflower.show()
    display_stats(sunflower)

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)
