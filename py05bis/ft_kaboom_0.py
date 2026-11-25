#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/15 18:29:16 by aantela-            #+#    #+#            #
#   Updated: 2026/11/16 13:26:51 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire import light_spell_record


def main() -> None:
    print("\n=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result = light_spell_record('Fantasy', 'Earth, Wind and fire')
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
