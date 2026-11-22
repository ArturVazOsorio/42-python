#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategies.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/21 15:41:14 by aantela-            #+#    #+#            #
#   Updated: 2026/11/22 17:21:18 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex3.creature import Creature, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class InvalidStrategyError(Exception):
    def __init__(self, creature: Creature):
        super().__init__(
            f"invalid Creature '{creature.name}' for this agressive strategy"
        )


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        raise InvalidStrategyError(creature)

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if isinstance(creature, TransformCapability):
            a, b = creature.transform(), creature.attack()
            c = creature.revert()
            return "\n".join([a, b, c])
        raise InvalidStrategyError(creature)

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
