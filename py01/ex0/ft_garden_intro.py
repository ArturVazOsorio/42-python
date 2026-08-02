#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/27 13:18:15 by aantela-         #+#    #+#              #
#    Updated: 2026/08/02 12:46:30 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_garden_intro():
    name = "Rose"
    height = 25
    age = 30
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    ft_garden_intro()
    print("=== End of Program ===")
