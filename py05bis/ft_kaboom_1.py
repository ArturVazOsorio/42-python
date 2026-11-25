#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/16 13:00:25 by aantela-            #+#    #+#            #
#   Updated: 2026/11/16 14:54:38 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    result: str = str(dark_spell_record("vodoo", "bats Frog and ball"))
    print(f"Testing record dark spell: {result}")


if __name__ == "__main__":
    main()
