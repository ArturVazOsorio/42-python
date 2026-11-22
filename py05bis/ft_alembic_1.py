#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_1.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 13:20:52 by aantela-            #+#    #+#            #
#   Updated: 2026/11/14 13:57:29 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy


def main() -> None:
    print("\n=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(
        f"Testing the"
        " hidden create_earth:"
        f"{alchemy.create_earth()}")  # type: ignore[attr-defined]


if __name__ == "__main__":
    main()
