# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/27 11:33:24 by aantela-         #+#    #+#              #
#    Updated: 2026/07/27 11:36:37 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    days = int(input("Day 1 harvest: "))
    days += int(input("Day 2 harvest: "))
    days += int(input("Day 3 harvest: "))
    print(f"Total harvest: {days}")
