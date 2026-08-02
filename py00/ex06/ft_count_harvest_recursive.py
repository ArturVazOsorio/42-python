# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/27 12:25:03 by aantela-         #+#    #+#              #
#    Updated: 2026/07/27 12:41:44 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive(days=None, current=1):
    if days is None:
        days = int(input("Days until harvest: "))
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    ft_count_harvest_recursive(days, current + 1)
