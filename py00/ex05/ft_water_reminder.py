# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/27 11:40:39 by aantela-         #+#    #+#              #
#    Updated: 2026/07/27 11:42:19 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
