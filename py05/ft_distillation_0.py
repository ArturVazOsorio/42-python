#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_0.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 14:52:45 by aantela-            #+#    #+#            #
#   Updated: 2026/11/14 15:10:27 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("\n=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_portion: {strength_potion()}")
    print(f"testing healing_portion: {healing_potion()}")


if __name__ == "__main__":
    main()
