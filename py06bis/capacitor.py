#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/21 15:13:44 by aantela-            #+#    #+#            #
#   Updated: 2026/11/21 15:35:06 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3 import CreatureFactory, TransformCreatureFactory
from ex3.creature import TransformCapability


def test_capacitor(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:", base.describe(), base.attack(), sep="\n")
    if isinstance(base, TransformCapability):
        print(base.transform(), base.attack(), base.revert(), sep="\n")
    print("evolved:", evolved.describe(), evolved.attack(), sep="\n")
    if isinstance(evolved, TransformCapability):
        print(
            evolved.transform(), evolved.attack(), evolved.revert(), sep="\n")


if __name__ == "__main__":
    print("Testing Creature with transform capability")
    tran = TransformCreatureFactory()
    test_capacitor(tran)
