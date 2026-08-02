#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/02 12:51:06 by aantela-         #+#    #+#              #
#    Updated: 2026/08/02 12:51:06 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.day} days old")


if __name__ == "__main__":
    plant1 = Plant(name="Rose", height=25, days=30)
    plant2 = Plant(name="Sunflower", height=80, days=45)
    plant3 = Plant(name="Cactus", height=15, days=120)
    print("=== Garden Plant Registry===")
    plant1.show()
    plant2.show()
    plant3.show()
