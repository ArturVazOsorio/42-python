#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_0.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 13:06:09 by aantela-            #+#    #+#            #
#   Updated: 2026/11/16 13:24:50 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import elements


def main() -> None:
    print("\n=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
