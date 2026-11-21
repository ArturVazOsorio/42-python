#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategies.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/21 15:41:14 by aantela-            #+#    #+#            #
#   Updated: 2026/11/21 15:43:01 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        ...

    @abstractmethod
    def is_valid(self) -> None:
        ...