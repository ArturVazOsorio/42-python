#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 15:11:00 by aantela-            #+#    #+#            #
#   Updated: 2026/11/14 15:15:26 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation.recipes


def main() -> None:
    print("\n=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    result = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead_to_gold: {result}")


if __name__ == "__main__":
    main()