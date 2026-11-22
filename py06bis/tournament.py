#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/22 16:17:39 by aantela-            #+#    #+#            #
#   Updated: 2026/11/22 17:25:13 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3 import FlameFactory, CreatureFactory, TransformCreatureFactory
from ex4 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, InvalidStrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    pairs = [
        f"({Cf.create_base().name}+"
        f"{Bs.__class__.__name__.replace('Strategy', '')})"
        for Cf, Bs in opponents]
    print(f"[ {', '.join(pairs)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            try:
                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]
                creature1 = factory1.create_base()
                creature2 = factory2.create_base()
                print("\n* Battle *")
                print(creature1.describe())
                print(" vs.")
                print(creature2.describe())
                print(" now fight!")
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    test_ok: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()), (TransformCreatureFactory(),
                                             AggressiveStrategy())]
    print("Tournament 0 (basic)")
    battle(test_ok)
    test_ko: list[tuple[CreatureFactory, BattleStrategy]] = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy())]
    print("Tournament 1 (error)")
    battle(test_ko)
