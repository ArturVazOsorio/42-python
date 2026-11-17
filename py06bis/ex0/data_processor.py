#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/17 02:21:32 by aantela-            #+#    #+#            #
#   Updated: 2026/11/17 02:43:52 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractclassmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0
        
    
    @abstractclassmethod
    def validate(self, data: Any)-> bool:
        pass
    
    @abstractclassmethod
    def ingest(self, data: Any) -> None:
        pass
    
    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data avaliable to output")
        item = self._data.pop(0)
        current_rank = self._rank
        self._rank += 1
        return (current_rank, item)
    
    
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        
    

