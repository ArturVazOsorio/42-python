# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/27 11:43:25 by aantela-         #+#    #+#              #
#    Updated: 2026/07/27 12:22:23 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    for x in range(day):
        print(f"Day {x + 1}")
    print("Harvest time!")
