#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 13:59:20 by aantela-            #+#    #+#            #
#   Updated: 2026/11/14 15:08:25 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"'{create_fire()}' and '{create_water()}'"
    )
