# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/27 11:37:54 by aantela-         #+#    #+#              #
#    Updated: 2026/07/27 11:39:43 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age >= 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
