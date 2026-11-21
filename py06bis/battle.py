#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/21 14:38:43 by aantela-            #+#    #+#            #
#   Updated: 2026/11/21 15:13:13 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3 import FlameFactory, TransformCreatureFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe(), base.attack(), sep="\n")
    print(evolved.describe(), evolved.attack(), sep="\n")


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    player1 = factory1.create_base()
    player2 = factory2.create_base()
    print(player1.describe(), " vs.", player2.describe(), " fight!", sep="\n")
    print(player1.attack(), player2.attack(), sep="\n")


if __name__ == "__main__":
    print("Testing factory")
    fire = FlameFactory()
    test_factory(fire)
    print("\nTesting factory")
    transform = TransformCreatureFactory()
    test_factory(transform)
    print("\nTesting battle")
    test_battle(fire, transform)
